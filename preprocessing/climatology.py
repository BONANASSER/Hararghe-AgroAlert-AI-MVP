"""
climatology.py
Physical climatology and hydrological accounting engine for Eastern Ethiopia:
1. Standardized Precipitation Index (SPI-1, SPI-3, SPI-6) via Gamma MLE fitting.
2. Two-layer soil water balance and CAFEC precipitation accounting for Sc-PDSI.
3. Vegetation Condition Index (VCI) calculation.
"""

import math
from typing import List, Tuple, Dict, Any
import numpy as np

def fit_gamma_parameters(precip_series: List[float]) -> Tuple[float, float, float]:
    """
    Fits a two-parameter Gamma distribution using Maximum Likelihood Estimation (MLE)
    with Thom's approximation (McKee et al., 1993).
    Returns (alpha, beta, q_zeros).
    """
    non_zeros = [x for x in precip_series if x > 0.0]
    n_total = len(precip_series)
    n_nonzero = len(non_zeros)
    
    if n_nonzero < 5:
        return 1.0, 1.0, 1.0 # Insufficient records
        
    q_zeros = (n_total - n_nonzero) / n_total
    mean_val = np.mean(non_zeros)
    log_mean = np.log(mean_val)
    mean_log = np.mean([np.log(x) for x in non_zeros])
    
    A = log_mean - mean_log
    if A <= 0:
        A = 1e-6
        
    # Thom's approximation for shape parameter alpha
    alpha = (1.0 + np.sqrt(1.0 + (4.0 * A / 3.0))) / (4.0 * A)
    beta = mean_val / alpha
    return float(alpha), float(beta), float(q_zeros)

def gamma_cdf(x: float, alpha: float, beta: float) -> float:
    """Computes the Gamma cumulative distribution function."""
    from scipy.special import gammainc
    if x <= 0:
        return 0.0
    return float(gammainc(alpha, x / beta))

def prob_to_z_score(p: float) -> float:
    """
    Transforms cumulative probability p in (0, 1) into standard normal deviate Z
    using Abramowitz & Stegun rational approximation.
    """
    p = max(1e-7, min(1.0 - 1e-7, p))
    if p > 0.5:
        p_eval = 1.0 - p
        sign = 1.0
    else:
        p_eval = p
        sign = -1.0
        
    t = math.sqrt(math.log(1.0 / (p_eval ** 2)))
    # Coefficients
    c0 = 2.515517
    c1 = 0.802853
    c2 = 0.010328
    d1 = 1.432788
    d2 = 0.189269
    d3 = 0.001308
    
    num = c0 + (c1 * t) + (c2 * (t ** 2))
    den = 1.0 + (d1 * t) + (d2 * (t ** 2)) + (d3 * (t ** 3))
    z = t - (num / den)
    return sign * z

def compute_spi(precip_series: List[float], target_precip: float) -> float:
    """Computes the Standardized Precipitation Index (SPI) for a given precipitation value."""
    alpha, beta, q = fit_gamma_parameters(precip_series)
    g_x = gamma_cdf(target_precip, alpha, beta)
    h_x = q + (1.0 - q) * g_x
    spi = prob_to_z_score(h_x)
    # Clip to standard meteorological range [-4.0, +4.0]
    return max(-4.0, min(4.0, round(spi, 2)))

class TwoLayerWaterBalance:
    """
    Implements Palmer's two-layer soil-water balance accounting:
    - Surface layer (Ss): Available water capacity = 25.4 mm (1.0 inch).
    - Sub-surface layer (Su): Available water capacity = AWC - Ss (defaults to 100 mm total AWC).
    """
    def __init__(self, awc: float = 100.0, ss_max: float = 25.4):
        self.awc = awc
        self.ss_max = ss_max
        self.su_max = max(10.0, awc - ss_max)
        self.ss = ss_max * 0.5 # Initial 50% saturation
        self.su = self.su_max * 0.5
        
    def step_month(self, precip_mm: float, pet_mm: float) -> Dict[str, float]:
        """
        Calculates one month of soil water accounting:
        P: Precipitation
        PE: Potential Evapotranspiration
        ET: Actual Evapotranspiration
        R: Recharge to soil layers
        RO: Runoff
        L: Soil moisture loss/drawdown
        """
        p = max(0.0, precip_mm)
        pe = max(0.0, pet_mm)
        
        if p >= pe:
            # Moisture surplus
            et = pe
            surplus = p - pe
            
            # Recharge surface layer first
            ss_deficit = self.ss_max - self.ss
            r_ss = min(surplus, ss_deficit)
            self.ss += r_ss
            surplus_rem = surplus - r_ss
            
            # Recharge sub-surface layer
            su_deficit = self.su_max - self.su
            r_su = min(surplus_rem, su_deficit)
            self.su += r_su
            
            recharge = r_ss + r_su
            runoff = surplus_rem - r_su
            loss = 0.0
        else:
            # Moisture deficit (p < pe)
            deficit = pe - p
            recharge = 0.0
            runoff = 0.0
            
            # Evaporate from surface layer first
            if self.ss >= deficit:
                loss_ss = deficit
                loss_su = 0.0
                self.ss -= loss_ss
            else:
                loss_ss = self.ss
                rem_deficit = deficit - self.ss
                self.ss = 0.0
                
                # Drawdown from sub-surface layer proportional to remaining capacity
                loss_su = min(self.su, rem_deficit * (self.su / self.su_max))
                self.su -= loss_su
                
            loss = loss_ss + loss_su
            et = p + loss
            
        storage_change = recharge - loss
        return {
            "P": round(p, 2),
            "PET": round(pe, 2),
            "ET": round(et, 2),
            "R": round(recharge, 2),
            "RO": round(runoff, 2),
            "L": round(loss, 2),
            "Ss": round(self.ss, 2),
            "Su": round(self.su, 2),
            "TotalSoilWater": round(self.ss + self.su, 2),
            "StorageChange": round(storage_change, 2)
        }

def compute_vci(ndvi_val: float, ndvi_min: float, ndvi_max: float) -> float:
    """Computes Vegetation Condition Index (VCI) in range [0, 100]%."""
    if ndvi_max <= ndvi_min:
        return 50.0
    vci = ((ndvi_val - ndvi_min) / (ndvi_max - ndvi_min)) * 100.0
    return max(0.0, min(100.0, round(vci, 1)))

if __name__ == "__main__":
    print("[CLIMATOLOGY] Testing SPI calculation...")
    sample_rain = [25.0, 40.0, 15.0, 0.0, 120.0, 180.0, 210.0, 195.0, 80.0, 20.0, 10.0, 5.0] * 3
    test_spi = compute_spi(sample_rain, 15.0)
    print(f"Sample drought SPI for 15 mm rain: {test_spi}")
    
    print("[CLIMATOLOGY] Testing 2-layer Soil Water Balance...")
    wb = TwoLayerWaterBalance(awc=100.0)
    step1 = wb.step_month(precip_mm=15.0, pet_mm=95.0)
    print(f"Step 1 deficit result: {step1}")
