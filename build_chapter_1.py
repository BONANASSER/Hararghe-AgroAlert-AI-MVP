"""
build_chapter_1.py
Chapter 1: Introduction and Research Motivation
"""

import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from build_master_concept_note import (
    add_heading_1, add_heading_2, add_heading_3, add_body, add_bullet, 
    add_callout, style_table, HEX_PRIMARY, HEX_SECONDARY, HEX_CALLOUT_BG
)

def build_chapter_1(doc):
    add_heading_1(doc, "CHAPTER ONE: INTRODUCTION AND RESEARCH MOTIVATION")
    
    # 1.1 Background
    add_heading_2(doc, "1.1 Background and Contextual Setting")
    add_body(doc, "Drought represents the single greatest recurring environmental and socioeconomic catastrophe threatening agrarian livelihoods across the Horn of Africa. In Ethiopia, where over 80% of the population relies directly on rainfed subsistence agriculture and pastoralism, hydro-climatic variability exerts an overwhelming control over national gross domestic product, food stability, and rural well-being. Over the past three decades, the frequency, duration, and spatial extent of severe drought shocks have escalated drastically, driven by global climate change and intensifying teleconnections with oceanic-atmospheric oscillations in the equatorial Pacific and Indian Oceans.")
    
    add_body(doc, "Eastern Ethiopia—and specifically Eastern Hararghe Zone in the Oromia Regional State—represents one of the most hydro-meteorologically vulnerable, ecologically fragile, and chronically food-insecure sub-regions in the country. Spanning steep topographic gradients from the highland plateaus of Deder, Girawa, and Kurfa Chele (over 3,000 meters above sea level) down to the arid and semi-arid agro-pastoral lowlands of Babile, Fedis, and Meyu Muluke bordering the Somali Region, Eastern Hararghe exhibits extreme microclimatic heterogeneity. The farming systems are dominated by subsistence cultivation of sorghum (Sorghum bicolor), maize (Zea mays), haricot beans (Phaseolus vulgaris), wheat, and barley, alongside high-value cash-crop khat (Catha edulis) and livestock husbandry. The region depends on a highly erratic bimodal rainfall regime comprising the Belg (short rainy season, March to May) and Kiremt / Deyr (main rainy season, June to September). A failure or severe delay in either season triggers rapid depletion of soil moisture, devastating crop desiccation, widespread livestock mortality, asset depletion, and acute human food crises.")
    
    add_body(doc, "The catastrophic reality of this vulnerability was demonstrated during the historic 2015–2016 El Niño-induced drought, which left more than 10.2 million Ethiopians requiring emergency food assistance, and the unprecedented 2020–2023 consecutive five-season drought across the eastern Horn. Most recently, in late 2025 and 2026, severe rainfall anomalies across the eastern highlands and lowlands precipitated another major humanitarian emergency, with FEWS NET and regional authorities projecting that over 20 million people required immediate external relief, with climate-induced agricultural collapse identified as the primary catalyst. These recurring emergencies expose an inescapable truth: reactive humanitarian relief operations, which mobilize months after crop desiccation and livestock mortality have already materialized, are economically unsustainable and fail to preserve human lives and livelihoods. What is urgently demanded is a proactive, localized, and actionable predictive early-warning system capable of forecasting impending hydro-climatic stress and acute food insecurity months before irreversible damage occurs.")

    # 1.2 Problem Statement
    add_heading_2(doc, "1.2 Statement of the Problem")
    add_body(doc, "Despite decades of substantial domestic and international investments in meteorological observatories, satellite remote sensing, and disaster risk management infrastructure, current operational early warning paradigms in Ethiopia remain fundamentally disconnected from the operational realities of smallholder farmers, local development agents, and humanitarian decision-makers. This operational paralysis stems from four interrelated, structural deficiencies:")
    
    add_bullet(doc, "Global Climate Models (GCMs) and conventional Regional Climate Models (RCMs) operate at coarse spatial resolutions ranging from 25 km to over 100 km. In highly dissected, topographically complex landscapes such as Eastern Hararghe, localized topoclimates, thermal inversions, rain-shadow phenomena, and elevation-dependent microclimates vary drastically across distances of only 1 to 5 km. Regional rainfall aggregates completely obscure local moisture deficits, rendering synoptic weather bulletins practically useless for plot-level agronomic management.", bold_prefix="1. The Spatial Resolution Disconnect: ")
    
    add_bullet(doc, "Conventional satellite-derived drought monitoring systems (e.g., standard NDVI anomalies, Vegetation Condition Index [VCI], and post-hoc remote sensing classifications) are fundamentally retrospective. They detect vegetation stress and canopy browning only after significant, irreversible cellular and physiological moisture deficit has already inflicted damage on crops. Smallholder farmers and extension personnel require forward-looking, lead-time intelligence (1 to 3 months prior to planting or during critical phenological stages) to make proactive decisions regarding crop selection, seed variety switching, planting dates, and water conservation investments.", bold_prefix="2. The Retrospective Monitoring Bias: ")
    
    add_bullet(doc, "Operational meteorological bulletins typically disseminate technical, abstract probabilistic metrics (e.g., 'a 35% probability of below-normal rainfall tercile') that fail to translate into actionable agronomic instructions. Farmers cannot determine whether such a forecast warrants switching from long-cycle maize to short-cycle sorghum, staggering planting dates, constructing tie-ridges, or rationing irrigation water. Crucially, conventional systems operate as top-down techno-scientific monoliths that systematically disregard centuries of Indigenous Ecological Knowledge (IEK) preserved by local farming communities, generating deep cultural skepticism, lack of trust, and near-zero advisory adoption in rural kebeles.", bold_prefix="3. The Socio-Technical Usability Gap: ")
    
    add_bullet(doc, "In existing institutional workflows, drought early warning (managed primarily by meteorological and hydrological agencies) is treated as completely separate from food insecurity early warning (conducted independently by humanitarian agencies such as FEWS NET and the IPC through periodic retrospective surveys). Physical hydro-meteorological models predict rainfall deficits but ignore socioeconomic vulnerability, livelihood zones, and market access; conversely, humanitarian food security assessments rely heavily on delayed surveys that cannot capture rapid environmental shifts. There is no unified, multimodal framework that directly models the cascading causal chain from global atmospheric forcing to local soil-water depletion, crop yield loss, and acute household food insecurity (IPC phases).", bold_prefix="4. The Analytical Decoupling of Environmental Hazard and Food Insecurity: ")

    # 1.3 Research Gaps
    add_heading_2(doc, "1.3 Research Gaps and Proposed Scientific Innovations")
    add_body(doc, "A systematic review of existing operational systems and published scientific literature highlights a critical research vacuum. While recent computational studies have explored machine learning for drought monitoring or regional food security (e.g., Busker et al., 2024; Baye et al., 2026; Abate et al., 2025), they either rely on coarse tabular aggregations across entire nations, examine individual modalities in isolation, fail to incorporate direct spatial image representation learning, or omit the physical climatological and teleconnection dynamics that govern East African climate.")
    
    add_body(doc, "Table 1.1 presents a comprehensive comparative synthesis distinguishing existing operational systems, published baseline studies, the foundational AgriMinds / AI-DREWS framework, and the transformative multimodal framework proposed in this thesis.")

    # Table 1.1: Comparative Synthesis Matrix
    gap_headers = ["Early Warning Dimension", "Conventional Systems (NMA / EDRMC)", "Regional ML Baselines (Busker; Baye)", "AgriMinds / AI-DREWS Baseline", "Proposed MSc Thesis Framework"]
    gap_widths = [Inches(1.3), Inches(1.2), Inches(1.3), Inches(1.3), Inches(1.4)]
    gap_data = [
        ["Geographic Scope & Unit", "National / Regional (25–100 km grid)", "Horn of Africa / National (Coarse Admin)", "Choke Mountain Watershed (8×8 Grid)", "Eastern Ethiopia / Eastern Hararghe (Woreda & Grid)"],
        ["Target Outcomes", "Rainfall terciles, static NDVI browning", "FEWS NET IPC food crisis (tabular)", "Drought hazard P(SPI-3<=-1) & Crop advisory", "Tri-Task: Drought P, Crop Advisory Risk, & IPC Food Insecurity"],
        ["Input Modalities", "Single-sensor rain/NDVI", "Heterogeneous tabular aggregates", "ERA5, CHIRPS, Niño indices, MODIS", "Satellite Patches (CNN) + Climate Series (LSTM) + FFT + Tabular MLP"],
        ["Climatological Physics", "Black-box statistical indices", "None (purely statistical ML)", "Sc-PDSI 2-layer balance, CAFEC, Niño Conv1D", "Sc-PDSI Climatology + Conv1D-LSTM ENSO + SoilGrids Edaphic Physics"],
        ["Agronomic Decision Support", "Generic qualitative bulletins", "None (humanitarian phase only)", "4-tier advisory matrix (Tef, Wheat, Maize)", "4-tier prescriptive matrix for Sorghum, Maize, Haricot, Wheat, Tef"],
        ["Traditional Knowledge (IEK)", "Completely ignored", "Completely ignored", "Bi-directional consensus engine (pilot)", "Formal bi-directional IEK consensus engine (Hararghe bio-cues)"],
        ["Explainability (XAI)", "Black-box", "SHAP on tabular variables only", "Feature importance metrics", "Multi-Level XAI: SHAP (tabular) + Grad-CAM (spatial CNN) + Temporal lags"],
        ["Knowledge Representation", "Relational database tables", "None", "Star schema for Metabase BI", "Neo4j Semantic Knowledge Graph (cascading hazard ontology)"],
        ["Validation & Lead Horizon", "Heuristic accuracy reporting", "Standard temporal cross-validation", "Honest Lead Horizon: Brier Skill Score (BSS)", "Honest Lead Horizon: BSS gating, Out-of-sample (2024–2026), Calibration"],
        ["User Delivery Architecture", "Static PDF bulletins / web portal", "Offline academic scripts", "FastAPI + Next.js + Offline Mobile", "Full Cloud FastAPI Microservice + Next.js 16 + Trilingual Offline Mobile"]
    ]
    tbl_gap = doc.add_table(rows=1, cols=5)
    style_table(tbl_gap, gap_widths, gap_headers, gap_data)

    # 1.4 Research Questions
    add_heading_2(doc, "1.4 Research Questions")
    add_heading_3(doc, "1.4.1 Primary Research Question")
    add_body(doc, "How can a super-hybrid multimodal deep learning framework effectively synthesize satellite Earth observation imagery, hydro-climatic teleconnections, vegetation dynamics, soil moisture, agricultural production statistics, and socioeconomic vulnerability data to generate localized, lead-time early warnings for drought hazards, prescriptive crop-level advisories, and acute food insecurity across Eastern Hararghe, Ethiopia?")
    
    add_heading_3(doc, "1.4.2 Specific Research Questions")
    add_bullet(doc, "Which physical hydro-climatic indicators (CHIRPS precipitation, SMAP soil moisture, MODIS LST/NDVI, ERA5 variables) and oceanic indices (Niño 3.4, IOD) exhibit the strongest teleconnection and predictive signal for agricultural drought in Eastern Hararghe?", bold_prefix="RQ1: ")
    add_bullet(doc, "How can multi-source, multi-resolution spatial rasters, temporal time series, and tabular socioeconomic data be harmonized into an immutable, cryptographically verifiable woreda-level data cube without temporal data leakage?", bold_prefix="RQ2: ")
    add_bullet(doc, "How effectively can specialized deep learning architectures (2D-CNN / ResNet for satellite patches, LSTM for temporal sequences, FFT for periodic harmonics, and MLP for tabular structures) extract modality-specific representations relative to standard unimodal baselines?", bold_prefix="RQ3: ")
    add_bullet(doc, "Does a multimodal gated cross-attention fusion architecture achieve statistically significant performance gains over concatenation, early fusion, and traditional tree-based models (XGBoost, Random Forest) in predicting drought and acute food insecurity?", bold_prefix="RQ4: ")
    add_bullet(doc, "How does model predictive skill evolve across forward forecast horizons (1, 2, and 3 months ahead), and at what forecast lead does the model cease to outperform local climatology under the Brier Skill Score (BSS)?", bold_prefix="RQ5: ")
    add_bullet(doc, "How can drought hazard probabilities be quantitatively modulated by crop-specific biological sensitivity coefficients (s) to generate actionable 4-tier prescriptive advisories for sorghum, maize, haricot bean, wheat, and tef?", bold_prefix="RQ6: ")
    add_bullet(doc, "How can a bi-directional consensus engine effectively reconcile deep learning risk predictions with Indigenous Ecological Knowledge (IEK) indicators (wind shifts, bird migrations, floral phenology) to establish community trust?", bold_prefix="RQ7: ")
    add_bullet(doc, "How can Explainable AI methods (SHAP, Grad-CAM, temporal attribution) and Neo4j semantic knowledge graphs be leveraged to make complex multimodal predictions interpretable for agricultural extension agents and policy makers?", bold_prefix="RQ8: ")

    # 1.5 Objectives
    add_heading_2(doc, "1.5 Research Objectives")
    add_heading_3(doc, "1.5.1 General Objective")
    add_body(doc, "To develop, empirically benchmark, and deploy an explainable, multimodal deep learning-based early warning system that integrates satellite Earth observations, hydro-climatic teleconnections, vegetation indices, soil moisture, agricultural statistics, and socioeconomic vulnerability to deliver localized drought predictions, prescriptive crop advisories, and acute food-insecurity forecasts in Eastern Hararghe, Ethiopia.")

    add_heading_3(doc, "1.5.2 Specific Objectives")
    add_bullet(doc, "To acquire, quality-control, and spatially-temporally harmonize multi-source datasets (NASA MODIS, CHIRPS v3, GPM IMERG, NASA SMAP, ECMWF ERA5, NOAA ERSSTv6, SoilGrids, WorldPop, CSA/ESS, and FEWS NET IPC) into a standardized woreda-month analytical cube with SHA-256 cryptographic provenance tracking.")
    add_bullet(doc, "To mathematically formulate and compute physical drought indices, including the two-layer Self-Calibrated Palmer Drought Severity Index (Sc-PDSI), Standardized Precipitation Index (SPI-1, 3, 6), and Vegetation Condition Index (VCI) for Eastern Hararghe.")
    add_bullet(doc, "To design and train a Conv1D-LSTM neural network to forecast equatorial Pacific Niño 3.4 sea surface temperature anomalies across 1 to 12 month leads to capture global teleconnection forcing.")
    add_bullet(doc, "To construct specialized deep neural encoders for spatial satellite patches (2D-CNN / ResNet), sequential environmental dynamics (LSTM), harmonic seasonal periodicity (Fast Fourier Transform), and tabular agricultural-socioeconomic structures (MLP).")
    add_bullet(doc, "To develop and evaluate a Multimodal Gated Cross-Attention Fusion Engine that integrates the learned latent representations into a unified context vector driving multi-task prediction heads for drought probability, crop risk, and IPC food security phases.")
    add_bullet(doc, "To implement and validate the 'Honest Lead Horizon' principle using the Brier Skill Score (BSS), strictly segregating quantitative probability mapping at Lead 1 from qualitative seasonal outlooks at Leads 2–3.")
    add_bullet(doc, "To formulate a Four-Tier Prescriptive Advisory Matrix coupling hazard probabilities with biological crop sensitivity coefficients (s) for sorghum, maize, haricot bean, wheat, and tef.")
    add_bullet(doc, "To build a Bi-Directional Indigenous Ecological Knowledge (IEK) Consensus Engine that validates AI forecasts against traditional bio-climatic indicators.")
    add_bullet(doc, "To integrate Explainable AI (SHAP for tabular/fusion features, Grad-CAM for satellite image saliency, temporal lag attributions) and construct a Neo4j Semantic Knowledge Graph representing cascading multi-hazard vulnerabilities.")
    add_bullet(doc, "To engineer and deploy an enterprise, cloud-native prototype ecosystem comprising a FastAPI microservice backend, PostgreSQL 17 Star Schema, Next.js 16 Web Command Centre, and an offline-first Expo React Native mobile field application in English, Amharic, and Afaan Oromoo.")

    # 1.6 Hypotheses
    add_heading_2(doc, "1.6 Research Hypotheses")
    add_bullet(doc, "A super-hybrid multimodal deep learning architecture integrating spatial satellite patches, temporal hydro-climatic sequences, harmonic cycles, and structured socioeconomic variables will achieve statistically superior predictive performance (higher ROC-AUC, PR-AUC, and Macro F1-score; lower RMSE) compared to single-modality models and conventional machine learning baselines (Random Forest, XGBoost).", bold_prefix="Hypothesis 1 (H1 - Multimodal Superiority): ")
    add_bullet(doc, "Coupling equatorial Pacific ENSO teleconnection forecasting (Conv1D-LSTM) with localized antecedent hydro-climatic memory significantly extends the skill horizon of drought early warning up to a 3-month lead time compared to local persistence or climatology baselines.", bold_prefix="Hypothesis 2 (H2 - Teleconnection Lead Extension): ")
    add_bullet(doc, "The integration of physical two-layer soil water balance accounting (Sc-PDSI) and biological crop sensitivity multipliers (s) significantly improves the agronomic fidelity and calibration of drought risk classification relative to purely meteorological rainfall anomaly metrics.", bold_prefix="Hypothesis 3 (H3 - Agronomic Calibration): ")
    add_bullet(doc, "Explainable AI attributions (SHAP feature values and Grad-CAM spatial heatmaps) will align with established agro-ecological domain principles, identifying root-zone moisture deficit, thermal stress, and vegetation anomaly as the primary drivers of impending acute food insecurity.", bold_prefix="Hypothesis 4 (H4 - XAI Domain Coherence): ")
    add_bullet(doc, "Cross-validating deep learning predictions with Indigenous Ecological Knowledge (IEK) through a bi-directional consensus engine increases community trust and intended advisory adoption rates among agricultural extension agents and smallholder farmers compared to un-contextualized probabilistic warnings.", bold_prefix="Hypothesis 5 (H5 - IEK Operational Adoption): ")

    # 1.7 Significance
    add_heading_2(doc, "1.7 Significance of the Study")
    add_body(doc, "The significance of this research spans multiple academic, practical, humanitarian, and policy dimensions:")
    add_bullet(doc, "Advances the frontier of multimodal representation learning in Earth observation and hydro-climatology by formulating a novel super-hybrid architecture that unifies 2D convolutional, recurrent sequential, harmonic spectral, and tabular deep learning paradigms.", bold_prefix="Scientific & Methodological Innovation: ")
    add_bullet(doc, "Transforms passive, abstract meteorological probability figures into plot-level, crop-tailored, prescriptive agronomic interventions that empower resource-poor farmers to take proactive, risk-mitigating actions months before harvest.", bold_prefix="Agronomic Resilience for Smallholders: ")
    add_bullet(doc, "Provides humanitarian relief agencies (FEWS NET, WFP, EDRMC) with localized, woreda-level predictive forecasts of acute food insecurity (IPC phases), transitioning disaster management from slow, expensive reactive relief to cost-effective anticipatory humanitarian action.", bold_prefix="Anticipatory Humanitarian Action: ")
    add_bullet(doc, "Pioneers the formal, computational integration of centuries-old Indigenous Ecological Knowledge with modern deep learning, demonstrating a culturally respectful, socio-technically sound pathway for AI adoption in the Global South.", bold_prefix="Indigenous Cultural Synthesis: ")
    add_bullet(doc, "Directly aligns with Ethiopia's Climate Resilient Green Economy (CRGE) strategy, the Green Legacy Initiative, and the Ministry of Agriculture's national digital extension transformation program (serving over 60,000 Development Agents nationwide).", bold_prefix="National Policy Alignment: ")

    # 1.8 Scope & Delimitations
    add_heading_2(doc, "1.8 Scope and Delimitations of the Study")
    add_body(doc, "The geographic scope of this study is strictly delineated to Eastern and Western Hararghe Zones (East Hararge and West Hararge) in the Oromia Regional State of Ethiopia, encompassing all constituent 41 administrative woredas (24 in East Hararge and 17 in West Hararge) extracted from official 2023 Ethiopian administrative boundary shapefiles. The primary spatial unit of analysis is the administrative woreda (Admin 3) and high-resolution geospatial grids covering the zones' complex topography.")
    add_body(doc, "The temporal scope comprises an unbroken, continuous 36-year and 10-month historical monitoring window from January 1990 to October 2026 across all input modalities (CHIRPS v3 satellite rainfall, MODIS/AVHRR vegetation greenness, SMAP/ERA5 soil moisture, ERA5 atmospheric reanalysis, and NOAA PSL ENSO teleconnection indices). Supervised acute food insecurity modeling is calibrated against historical and contemporary FEWS NET / IPC classification records across the 1990–2026 window, providing an empirical panel of 18,122 woreda-month observations.")
    add_body(doc, "Delimitation: This research explicitly develops an analytical and decision-support prototype. It does not intend to replace official statutory declarations of drought or famine issued by the Ministry of Agriculture, the Ethiopian Disaster Risk Management Commission (EDRMC), or the formal multi-agency IPC Technical Working Group. Furthermore, while the model identifies predictive associations and feature attributions via XAI, it strictly avoids unwarranted causal claims.")

    # 1.9 Operational Definitions
    add_heading_2(doc, "1.9 Operational Definitions of Key Terms")
    terms = [
        ("Multimodal Deep Learning", "An artificial intelligence architecture that ingests and processes heterogeneous data modalities (spatial rasters, temporal sequences, harmonic spectra, and structured tabular records) via specialized neural encoders and unifies them through a fused latent representation."),
        ("Super-Hybrid Architecture", "A tri-branch or multi-branch neural network combining 2D-CNNs for spatial feature extraction, LSTMs for recurrent temporal memory, and Fast Fourier Transforms (FFT) for periodic/astronomical cycle modeling."),
        ("Self-Calibrated Palmer Drought Severity Index (Sc-PDSI)", "A physically based hydro-meteorological drought index that models soil water balance across a two-layer soil profile (surface layer: 25.4 mm; sub-surface layer: configurable AWC) and dynamically calibrates climatic characteristics to local station conditions."),
        ("Standardized Precipitation Index (SPI)", "A multi-scalar meteorological drought index expressing the number of standard deviations that observed cumulative precipitation deviates from the long-term climatological probability distribution over a specified time scale (e.g., SPI-1, SPI-3, SPI-6)."),
        ("Vegetation Condition Index (VCI)", "A satellite-derived remote sensing metric that normalizes the Normalized Difference Vegetation Index (NDVI) between its historical minimum and maximum for a given calendar period, reflecting vegetation vigor relative to historical extremes."),
        ("Atmospheric Teleconnection", "A recurring, persistent large-scale pattern of atmospheric pressure and circulation anomalies spanning vast geographical distances, specifically linking equatorial Pacific sea surface temperatures (ENSO) and Indian Ocean Dipole (IOD) to rainfall anomalies in Eastern Ethiopia."),
        ("Integrated Food Security Phase Classification (IPC)", "A standardized, five-phase analytical scale used globally by humanitarian agencies to classify the severity of acute food insecurity: Phase 1 (Minimal), Phase 2 (Stressed), Phase 3 (Crisis), Phase 4 (Emergency), and Phase 5 (Catastrophe/Famine)."),
        ("Crop Sensitivity Coefficient (s)", "A species-specific biological multiplier that scales physical drought hazard probability based on the phenological vulnerability and moisture stress tolerance of specific crops (e.g., tef s=0.8, wheat s=1.0, maize s=1.3)."),
        ("Honest Lead Horizon Principle", "An operational forecasting doctrine enforcing that quantitative spatial risk maps are served only at lead times achieving statistically significant positive skill relative to climatology (Brier Skill Score BSS > 0), while distant leads are served solely as qualitative directional outlooks."),
        ("Brier Skill Score (BSS)", "A verification metric quantifying the relative accuracy of probabilistic forecasts compared to a reference baseline (long-term climatology), where positive scores denote genuine predictive skill superiority."),
        ("Indigenous Ecological Knowledge (IEK)", "A cumulative body of empirical observations, practices, and beliefs developed over generations by local communities regarding seasonal transitions, wind shifts, celestial movements, bird migrations, and plant phenology."),
        ("Bi-Directional Consensus Engine", "An algorithmic framework that cross-validates quantitative deep learning predictions against qualitative community-submitted traditional bio-climatic indicators to classify consensus state and calibrate operational confidence."),
        ("Explainable AI (XAI)", "A suite of machine learning algorithms (such as SHAP and Grad-CAM) designed to provide human-interpretable explanations of the mathematical reasoning, feature contributions, and spatial regions governing a neural network's predictions."),
        ("Knowledge Graph", "A semantic graph database (implemented in Neo4j) that represents real-world entities (woredas, crops, hazards, climate records, relief programs) and their interconnected relationships as nodes and directed edges for contextual reasoning."),
        ("Woreda-Month", "The fundamental spatiotemporal unit of analysis in this thesis, defining an administrative woreda observed across an individual monthly calendar window.")
    ]
    for term, definition in terms:
        add_bullet(doc, definition, bold_prefix=f"{term}: ")

    # 1.10 Organization of Thesis
    add_heading_2(doc, "1.10 Organization of the Concept Note / Thesis Proposal")
    add_body(doc, "This concept note is organized into five comprehensive chapters. Chapter One presents the introduction, problem statement, research gaps, questions, objectives, hypotheses, significance, and scope. Chapter Two provides the theoretical foundations and conceptual framework, reviewing physical climatology, teleconnections, multimodal deep learning, XAI, knowledge graphs, and IEK. Chapter Three establishes the detailed research methodology, technical architecture, data ingestion registry, model formulations, validation protocols, and software deployment pipeline. Chapter Four outlines the research work plan, timeline, resource requirements, and risk mitigation strategies. Chapter Five compiles the comprehensive academic references, followed by five technical appendices containing the master data schema, mathematical proofs, experimental comparison matrices, Cypher graph schemas, and software architecture specifications.")

    doc.add_page_break()

print("Chapter 1 module defined.")
