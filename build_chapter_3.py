"""
build_chapter_3.py
Chapter 3: Research Methodology and Technical Architecture
"""

import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from build_master_concept_note import (
    add_heading_1, add_heading_2, add_heading_3, add_body, add_bullet, 
    add_callout, style_table, HEX_PRIMARY, HEX_SECONDARY, HEX_CALLOUT_BG
)

def build_chapter_3(doc):
    add_heading_1(doc, "CHAPTER THREE: RESEARCH METHODOLOGY AND TECHNICAL ARCHITECTURE")
    
    # 3.1 Study Area
    add_heading_2(doc, "3.1 Study Area Delineation and Agro-Ecological Characterization")
    add_body(doc, "The study area is located in Eastern Ethiopia, encompassing both the Eastern Hararghe (East Hararge) and Western Hararghe (West Hararge) Administrative Zones within the Oromia Regional State. Geographically, this combined study region extends approximately between 7°32′ N to 9°48′ N latitude and 40°15′ E to 43°16′ E longitude, covering an extensive and topographically dissected area of over 45,000 km² bordering the Afar Regional State and Dire Dawa to the north, Somali Regional State to the east and south, and Arsi and West Arsi Zones to the west.")
    
    add_body(doc, "The terrain exhibits a precipitous elevation gradient spanning from over 3,400 meters above sea level in the high-altitude peaks of Gara Muleta and the Chercher mountain ranges down to 500 meters in the semi-arid lowland river basins draining toward the Awash and Wabe Shebelle. This profound vertical relief establishes three sharply demarcated agro-ecological zones across all 41 woredas (24 woredas in East Hararge and 17 woredas in West Hararge, extracted directly from official 2023 Ethiopian administrative boundary shapefiles):")
    
    add_bullet(doc, "Low-altitude valleys and plains (< 1,500 m a.s.l.) characterized by high mean temperatures (25°C–34°C), high potential evapotranspiration, shallow sandy soils, and erratic rainfall (350–600 mm/year). Encompasses Babile, Fedis, Chinaksen, Midhaga Tola, Meyu Muleke, Kumbi, Golo Oda in East Hararge; and Mieso, Hawi Gudina, Gumbi Bordede, Daro Lebu, Boke in West Hararge. Farming is dominated by drought-tolerant sorghum, short-cycle millet, sesame, and pastoral camel and goat husbandry. Highly prone to severe meteorological and agricultural moisture deficits.", bold_prefix="1. Kolla (Warm Semi-Arid Lowlands / Agro-Pastoral): ")
    add_bullet(doc, "Mid-altitude plateaus and undulating hills (1,500–2,300 m a.s.l.) featuring moderate temperatures (18°C–24°C), fertile vertisols and cambisols, and moderate rainfall (600–900 mm/year). Encompasses Haro Maya, Kersa, Kombolcha, Meta, Gursum, Jarso, Bedeno in East Hararge; and Habro, Anchar, Goba Koricha, Kuni/Oda Bultum, Chiro Zuria in West Hararge. Represents the agricultural heartland, supporting intensive mixed smallholder production of sorghum, maize, haricot beans, intercropped vegetables, and high-value cash-crop khat (Catha edulis).", bold_prefix="2. Woina Dega (Temperate Midlands): ")
    add_bullet(doc, "Highland ridges and plateaus (2,300–3,400 m a.s.l.) characterized by cool thermal regimes (10°C–18°C), andosols and luvisols, and higher rainfall (900–1,200 mm/year). Encompasses Deder, Girawa, Kurfa Chele in East Hararge; and Mesela, Doba, Tulo, Gemechis in West Hararge. Dominated by bread wheat, barley, faba beans, field peas, and highland potatoes. Vulnerable to early-season dry spells and terminal moisture deficits.", bold_prefix="3. Dega (Cool Sub-Humid Highlands): ")

    add_body(doc, "Administratively, the zone encompasses over 18 rural woredas, including Babile, Fedis, Gursum, Jarso, Kersa, Deder, Meta, Haramaya, Kombolcha, Girawa, Bedeno, Kurfa Chele, Chinaksen, Midhaga Tola, Meyu Muluke, Kumbi, Golo Oda, and Bate. The zone experiences a bimodal precipitation regime: the Belg (short rainy season, March to May) vital for land preparation and long-cycle cereal sowing, and the Kiremt / Meher (main monsoon rains, June to September) accounting for over 70% of crop biomass production. In the southern agro-pastoral woredas, rainfall follows the equatorial bimodal Gu/Genna (April–June) and Deyr/Karan (October–November) cycle. This dual exposure makes Eastern Hararghe an ideal living laboratory for multimodal drought and food-insecurity early warning research.")

    # 3.2 System Architecture
    add_heading_2(doc, "3.2 End-to-End System Architecture Overview")
    add_body(doc, "The technical architecture of the platform is designed as an end-to-end, multi-tiered operational pipeline bridging global oceanic-atmospheric forcing to plot-level farmer action and regional policy response, as summarized below:")

    arch_headers = ["Operational Tier", "Functional Architecture", "Core Components & Technologies", "Primary Data & Process Outputs"]
    arch_widths = [Inches(1.2), Inches(1.6), Inches(1.9), Inches(1.8)]
    arch_data = [
        ["Tier 1: Data Ingestion", "Automated Zero-Credential Ingestion Pipeline", "NOAA PSL, ECMWF Open-Meteo, CHIRPS, SMAP, MODIS, FAOSTAT, FEWS NET; SHA-256 Manifest Engine", "Raw multi-sensor archives with immutable cryptographic checksums in data/raw/"],
        ["Tier 2: Preprocessing", "Spatial Harmonization & Feature Engineering", "GDAL/Rasterio, GeoPandas, WGS84 Woreda Polygon Masking, 8×8 Catchment Grid, Sc-PDSI Climatology Engine", "Master analytical Woreda × Month data cube, 30-year anomalies, multi-timescale SPI/VCI tensors"],
        ["Tier 3: Super-Hybrid ML", "Multimodal Deep Learning Predictive Engine", "Conv1D-LSTM ENSO Forecaster + 2D-CNN Image Patch Encoder + LSTM Sequence Encoder + FFT + Gated Cross-Attention", "Multi-task logits: Drought Probability P(SPI-3<=-1), Crop Risk Index, IPC Food Insecurity Phase"],
        ["Tier 4: Decision Support", "Prescriptive Advisory, IEK Consensus & XAI", "Crop Sensitivity Multipliers (s), 4-Tier Prescriptive Matrix, Bi-Directional IEK Engine, SHAP, Grad-CAM, Neo4j KG", "Actionable farm-level advisories, traditional consensus flags, feature explanations, semantic graph queries"],
        ["Tier 5: Delivery Ecosystem", "Cloud-Native Multi-Tenant Enterprise Interface", "FastAPI Async API, PostgreSQL 17 Star Schema, Next.js 16 Web Command Centre, Trilingual Expo Mobile (EN/AM/OR)", "Role-scoped web dashboards (/ministry, /farm), offline-first field app, Metabase BI analytics"]
    ]
    tbl_arch = doc.add_table(rows=1, cols=4)
    style_table(tbl_arch, arch_widths, arch_headers, arch_data)

    # 3.3 Data Ingestion Registry
    add_heading_2(doc, "3.3 Multi-Source Data Ingestion Registry and Provenance Architecture")
    add_body(doc, "To ensure complete scientific transparency, zero-credential reproducibility, and immutable data provenance, every raw dataset ingested into the pipeline is sourced from publicly accessible, internationally recognized scientific repositories requiring no commercial API tokens. Table 3.2 details the complete multi-source data registry:")

    # Table 3.2: Data Registry
    reg_headers = ["Input Dataset", "Primary Provider / Portal", "Spatial / Temporal Res.", "Temporal Coverage", "Specific Role in Modeling Continuum"]
    reg_widths = [Inches(1.3), Inches(1.4), Inches(1.1), Inches(1.1), Inches(1.6)]
    reg_data = [
        ["Niño 3.4, 1+2, 4, SOI", "NOAA Physical Sciences Lab (ERSST v6)", "Equatorial Pacific / Monthly", "1990–2026", "Global oceanic-atmospheric forcing & ENSO teleconnection modeling"],
        ["CHIRPS v3 Precipitation", "Climate Hazards Center (UCSB / SERVIR)", "0.05° (~5 km) / Daily & Monthly", "1990–2026", "Primary precipitation history, SPI-1/3/6 calculation, rainfall anomalies"],
        ["NASA GPM IMERG V07", "NASA GES DISC (3IMERGDF)", "0.1° (~10 km) / Daily", "2000–2026", "Independent satellite precipitation validation & near-real-time cross-checking"],
        ["NASA SMAP L3 Moisture", "NASA NSIDC DAAC (SPL3SMP_E)", "9 km EASE-Grid / Daily", "2015–2026", "Root-zone and surface soil-moisture drawdown & agricultural drought dynamics"],
        ["MODIS MOD13Q1 V6.1", "NASA LP DAAC / USGS Earthdata", "250 m / 16-Day Composite", "2000–2026", "Vegetation greenness (NDVI, EVI), VCI, crop phenological canopy stress"],
        ["MODIS MOD11A2 V6.1", "NASA LP DAAC / USGS Earthdata", "1 km / 8-Day Composite", "2000–2026", "Daytime & nighttime Land Surface Temperature (LST), thermal stress anomalies"],
        ["ERA5 Reanalysis", "ECMWF / Copernicus CDS / Open-Meteo", "0.25° (~31 km) / Daily & Monthly", "1990–2026", "2 m temperature, potential evapotranspiration (PET), 10 m wind vectors (u, v)"],
        ["SoilGrids Edaphic Data", "ISRIC Global Soil Information", "250 m / Static Spatial Grid", "Static Baseline", "Soil water capacity (AWC), texture, clay %, organic carbon (SOC), pH"],
        ["WorldPop Demographics", "WorldPop / University of Southampton", "100 m / Annual Grid", "2015–2026", "Woreda-level population density, human exposure, and demographic vulnerability"],
        ["Agricultural Statistics", "Central Statistical Agency (CSA/ESS)", "Woreda-Zone / Annual", "2015–2026", "Cultivated area, crop production, crop yield baselines for staple cereals"],
        ["FEWS NET IPC Classifications", "FEWS NET Data Explorer / IPC Global", "Livelihood Zone / Woreda / Quarterly", "2015–2026", "Supervised acute food insecurity targets: IPC Phase 1 (Minimal) to Phase 5 (Famine)"]
    ]
    tbl_reg = doc.add_table(rows=1, cols=5)
    style_table(tbl_reg, reg_widths, reg_headers, reg_data)

    add_heading_3(doc, "3.3.1 Cryptographic Data Integrity and Provenance Manifests")
    add_body(doc, "A critical hazard in machine learning research is the inadvertent contamination of real meteorological forecasts with synthetic demonstration fixtures or uncalibrated mock records. AgriMinds enforces a strict cryptographic manifest system (data/raw/manifests/dataset.json). Whenever 'make ingest' or 'ai-drews ingest all' executes, each connector downloads the verified public archives, computes SHA-256 cryptographic checksums, logs exact URL endpoints, record counts, and timestamps. At runtime, the inference engine inspects dataset.json: if the manifest is absent or contains synthetic mock flags, all API payloads and UI views strictly append 'provenance: { data_source: synthetic, status: demonstration }' and display warning banners. Only when verified observational records are present does the system issue official early warning bulletins.")

    # 3.4 Spatial Harmonization
    add_heading_2(doc, "3.4 Spatial-Temporal Harmonization and Feature Engineering")
    add_body(doc, "Data harmonization transforms heterogeneous raw formats (NetCDF4, GeoTIFF, HDF5, CSV, and Shapefiles) into an aligned spatiotemporal data cube structured as Woreda × Month:")
    add_bullet(doc, "All spatial rasters are reprojected to the standard WGS84 geographic coordinate reference system (EPSG:4326). Using authoritative administrative polygons from the Ethiopian Statistical Service and FEWS NET, zonal statistics (mean, median, standard deviation, 10th and 90th percentiles) are extracted for each woreda polygon. For spatial deep learning branches, standardized 32×32 pixel multi-spectral image patches centered over each woreda centroid are sliced from 250 m MODIS grids.", bold_prefix="Spatial Alignment & Patch Extraction: ")
    add_bullet(doc, "Sub-monthly observations (daily CHIRPS/GPM, 8-day LST, 16-day NDVI) are aggregated into uniform monthly calendar windows and standard 10-day dekadal intervals. Temporal lags spanning 1, 2, 3, and 6 months are generated strictly using historical observations available prior to the prediction timestamp t to prevent look-ahead bias.", bold_prefix="Temporal Resampling & Lag Generation: ")
    add_bullet(doc, "Climatological normals are computed for each calendar month across the 30-year baseline (1990–2020). Standardized anomalies are derived as: Anomaly_{m,t} = [X_{m,t} - μ_{m}] / σ_{m}, where μ and σ represent the long-term monthly mean and standard deviation.", bold_prefix="Anomaly Normalization: ")

    # 3.5 Proposed Deep Learning Architecture
    add_heading_2(doc, "3.5 Proposed Super-Hybrid Multimodal Deep Learning Architecture")
    add_body(doc, "The computational intelligence of the proposed early warning system is organized around two tightly coupled neural frameworks: (1) an antecedent Conv1D-LSTM ENSO Forecaster, and (2) a Super-Hybrid Multimodal Deep Learning Model featuring specialized modality encoders and a Gated Cross-Attention Fusion Engine, as detailed below:")

    add_heading_3(doc, "3.5.1 Objective 1: Conv1D-LSTM ENSO Teleconnection Forecaster")
    add_body(doc, "Objective 1 forecasts equatorial Pacific Niño 3.4 sea surface temperature anomalies across 1 to 12 forward leads (L=12) from a 12-month antecedent sequence of four monthly Pacific climate indices: X in R^{B x 12 x 4}, where x_t = [Niño 3.4, Niño 1+2, Niño 4, SOI]^T. The architecture comprises:")
    add_bullet(doc, "Two 1D Convolutional layers (Conv1D) with 32 filters, kernel size = 3, stride = 1, padding = 1, followed by ReLU activation and Batch Normalization. These layers extract short-term ocean-atmosphere momentum and rate-of-change dynamics across the sequence.")
    add_bullet(doc, "A recurrent LSTM layer with 64 hidden units that processes the 12-step feature map sequence, capturing lagged multi-month oceanic memory and thermodynamic heat content buildup.")
    add_bullet(doc, "A dense multi-layer perceptron projection head (Dense(64 -> 32) -> ReLU -> Dropout(0.2) -> Dense(32 -> L)) emitting predicted Niño 3.4 anomalies y_hat in R^L across forward forecast leads 1 to 12.")

    add_heading_3(doc, "3.5.2 Objective 2: Super-Hybrid Multimodal Early Warning Model")
    add_body(doc, "The localized prediction model processes five complementary branches that simultaneously capture spatial gradients, temporal memory, periodic harmonics, and structured vulnerability:")
    
    add_bullet(doc, "Receives standardized 4-channel spatial raster patches (MODIS NDVI, EVI, Daytime LST, Nighttime LST) centered over the target woreda. Built upon a modified ResNet-50 backbone with the classification head removed, outputting a 64-dimensional spatial embedding vector e_spatial.", bold_prefix="1. Spatial Visual Branch (Xs in R^{B x C x H x W}): ")
    
    add_bullet(doc, "Processes multi-month sequential time series (T=12 antecedent months) of basin hydro-climatic variables: CHIRPS precipitation, SMAP surface soil moisture, ERA5 2 m temperature, and 10 m wind vector components (u, v). An LSTM network (hidden dimension = 64) recursively models the sequence, emitting the final hidden state h_last as a 64-dimensional temporal embedding vector e_temporal.", bold_prefix="2. Recurrent Temporal Branch (Xt in R^{B x T x F_t}): ")
    
    add_bullet(doc, "Applies a Fast Fourier Transform (FFT) across multi-year monthly precipitation and temperature series to extract dominant spectral amplitudes and phases. A linear layer (Linear(F_p -> 32) -> ReLU) projects the top Fourier frequencies into a 32-dimensional harmonic embedding e_periodic, encoding seasonal cycles and bi-annual Belg/Kiremt transitions.", bold_prefix="3. Periodic / Harmonic Spectral Branch (Xp in R^{B x F_p}): ")
    
    add_bullet(doc, "Ingests structured tabular features, including agricultural production statistics (crop area, historical yield baseline), demographic density (WorldPop), and static soil edaphic properties (SoilGrids AWC, pH, clay, SOC). Processed via a three-layer MLP (Linear(F_tab -> 64) -> BatchNorm -> ReLU -> Dropout(0.3) -> Linear(64 -> 32)) yielding a 32-dimensional context embedding e_tabular.", bold_prefix="4. Structured Tabular Branch (Xd in R^{B x F_tab}): ")
    
    add_bullet(doc, "Rather than naive vector concatenation, the four latent embeddings [e_spatial (64), e_temporal (64), e_periodic (32), e_tabular (32)] are projected into a common d_model = 64 dimensional representation space. A Multi-Head Cross-Attention layer computes dynamic cross-modal attention matrices, allowing temporal climate anomalies to query spatial vegetation patches and tabular soil properties. Gated skip-connections regulate information flow, yielding a unified 128-dimensional multimodal context vector g_fused.", bold_prefix="5. Multimodal Gated Cross-Attention Fusion Engine: ")

    add_heading_3(doc, "3.5.3 Multi-Task Output Prediction Heads")
    add_body(doc, "The fused context vector g_fused is routed to three specialized prediction heads operating simultaneously:")
    add_bullet(doc, "Emits the quantitative probability of meteorological-agricultural drought occurrence across forward leads L (1, 2, 3 months): P(SPI-3 <= -1.0) and P(Sc-PDSI <= -2.0) via a Sigmoid activation.", bold_prefix="Head A: Physical Drought Hazard Probability: ")
    add_bullet(doc, "Computes the biological sensitivity-adjusted drought risk P_adj across staple regional crops, modulating hazard probabilities by species sensitivity coefficients s.", bold_prefix="Head B: Prescriptive Crop Risk Index: ")
    add_bullet(doc, "Emits a 5-class probability distribution across FEWS NET / IPC acute food insecurity phases (Phase 1: Minimal, Phase 2: Stressed, Phase 3: Crisis, Phase 4: Emergency, Phase 5: Catastrophe) via a Softmax layer.", bold_prefix="Head C: Acute Food Insecurity Classification: ")

    # 3.6 Crop Sensitivity & Prescriptive Advisory
    add_heading_2(doc, "3.6 Crop Sensitivity Phenology and 4-Tier Prescriptive Advisory Matrix")
    add_body(doc, "A drought prediction provides zero operational value to a smallholder farmer if it is communicated as an abstract statistical metric without actionable instructions. In AgriMinds, physical drought hazard probability P is translated into crop-tailored operational decisions by applying biological crop sensitivity multipliers (s) encoded in the agronomic rules engine (ml/src/ai_drews/advisory/rules.py). Table 3.3 details the phenological vulnerability profiles and management parameters:")

    # Table 3.3: Crop Advisory Profiles
    crop_headers = ["Crop Species", "Biological Sensitivity (s)", "Critical Phenological Vulnerability Window", "Optimal Agronomic Sowing & Management Protocols"]
    crop_widths = [Inches(1.2), Inches(1.1), Inches(1.9), Inches(2.3)]
    crop_data = [
        ["Sorghum (Sorghum bicolor)", "s = 0.9 (Moderate)", "Flowering and early grain milk stage; highly drought-resistant during vegetative stage due to deep root system.", "Sowing: Mid-May (midlands) to late June (lowlands). Tolerates dry spells; prioritize tied-ridging and in-situ rainwater harvesting."],
        ["Maize (Zea mays)", "s = 1.3 (Very High)", "Tasseling, silking, and early grain filling. Moisture stress during silking causes pollination failure and catastrophic barren stalks.", "Sowing: Late April to mid-May for long-cycle varieties; switch immediately to ultra-early maturing varieties or tef/sorghum if Belg rains fail."],
        ["Haricot Bean (Phaseolus vulgaris)", "s = 1.1 (High)", "Flowering, pod initiation, and pod filling. Susceptible to flower shedding and abortion under moisture stress.", "Sowing: Early to mid-July. Ideal intercrop with sorghum or maize; provides soil nitrogen fixation and risk diversification."],
        ["Bread Wheat (Triticum aestivum)", "s = 1.0 (Baseline)", "Crown root initiation (CRI, 20–25 days post-sowing), booting, and anthesis. Moderate drought tolerance in vertisols.", "Sowing: Mid-June to early July. Staggered planting mitigates mid-season moisture deficits; prioritize supplemental deficit irrigation at CRI."],
        ["Tef (Eragrostis tef)", "s = 0.8 (Resilient)", "Panicle emergence and heading. Shallow rooting but highly versatile; tolerates waterlogging and late-season dry spells.", "Sowing: Mid to late July. Acts as the primary emergency catch-crop when early Belg/Kiremt rains fail and maize aborts."]
    ]
    tbl_crop = doc.add_table(rows=1, cols=4)
    style_table(tbl_crop, crop_widths, crop_headers, crop_data)

    add_body(doc, "The adjusted risk probability P_adj = min(P * s, 1.0) maps onto a Four-Tier Operational Advisory Action Matrix, triggering concrete, verified farm-management interventions:")
    add_bullet(doc, "Proceed with certified high-yielding full-season varieties. Standard fertilizer application packages (NPS/Urea). Standard moisture conservation (contour plowing, conservation tillage).", bold_prefix="1. Low Risk (P_adj < 0.25): ")
    add_bullet(doc, "Prioritize certified early-maturing and drought-escaping seed varieties. Conduct seed priming (pre-soaking seeds to accelerate germination). Construct in-situ soil moisture structures (tie-ridging, contour bunding, micro-basins). Monitor dekadal agro-meteorological bulletins with kebele development agents.", bold_prefix="2. Moderate Risk (0.25 <= P_adj < 0.45): ")
    add_bullet(doc, "Crop species substitution: pivot acreage from vulnerable long-cycle maize to drought-hardy sorghum or tef. Stagger sowing dates across fragmented plots to hedge against dry spells. Delay planting until cumulative soil moisture recharge exceeds 25 mm. Activate deficit irrigation schedules on irrigable plots. Establish community livestock fodder reserves.", bold_prefix="3. High Risk (0.45 <= P_adj < 0.65): ")
    add_bullet(doc, "Emergency agronomic pivot: abort long-cycle cereal cultivation; switch 100% of cultivated area to ultra-short-cycle pulses (haricot bean, chickpea) or drought-tolerant tef. Restrict water applications strictly to homestead high-density nursery plots. Secure livestock via destocking or migration to designated drought reserves. Trigger early shock-responsive safety-net programs (Productive Safety Net Programme [PSNP]) and release strategic woreda grain reserves.", bold_prefix="4. Severe Risk (P_adj >= 0.65): ")

    # 3.7 IEK Consensus Engine
    add_heading_2(doc, "3.7 Bi-Directional Indigenous Ecological Knowledge (IEK) Consensus Engine")
    add_body(doc, "Scientific forecasts are frequently rejected by rural pastoral and agrarian communities when perceived as opaque, top-down edicts disconnected from cultural traditions. AgriMinds bridges this divide through a Bi-Directional IEK Consensus Engine. Agricultural extension agents and lead farmers submit observed local bio-climatic indicators via the offline-first mobile application:")
    add_bullet(doc, "Dry, dust-laden easterly winds indicate prolonged dry spells; steady, moist southwesterly winds signaling Kiremt monsoon onset; dense morning mist lingering on Gara Muleta mountain summits indicating imminent rainfall.", bold_prefix="Atmospheric Indicators: ")
    add_bullet(doc, "Arrival and nesting of the Abdim's Stork (Ciconia abdimii, 'Shimela') signaling reliable rain within 10–14 days; aberrant bird migratory retreats indicating impending drought; aggressive honeybee swarming and foraging intensity.", bold_prefix="Faunal Indicators: ")
    add_bullet(doc, "Abnormal profuse flowering of Acacia bussei, Acacia tortilis, and Hagenia abyssinica before the rains denoting impending severe dry spells (trees responding to stress).", bold_prefix="Floral Phenology: ")

    add_body(doc, "The IEK consensus algorithm compares the AI-predicted hazard state with the aggregated community traditional observation index, assigning one of three operational consensus states:")
    add_bullet(doc, "Both the AI model and traditional indicators agree (e.g., both signal high drought hazard or both signal favorable rainfall). Model confidence is elevated to HIGH, and prescriptive action packages are issued with joint endorsement.", bold_prefix="1. High Consensus (Confidence = HIGH): ")
    add_bullet(doc, "One system indicates moderate stress while the other indicates near-normal conditions. Confidence is marked MODERATE, and weekly field monitoring by development agents is scheduled.", bold_prefix="2. Moderate Consensus (Confidence = MODERATE): ")
    add_bullet(doc, "The AI deep learning model predicts severe drought while traditional cues indicate heavy rainfall (or vice versa). Confidence is marked DIVERGENT; the system immediately issues an automated ground-inspection task to woreda agricultural supervisors to verify local soil moisture and rain gauges before broadcasting mass alerts.", bold_prefix="3. Divergent Consensus (Flag = GROUND INSPECTION TRIGGERED): ")

    # 3.8 Explainable AI
    add_heading_2(doc, "3.8 Explainable Artificial Intelligence (XAI) Implementation")
    add_body(doc, "The XAI framework provides multi-level interpretability across tabular, spatial, and temporal dimensions:")
    add_bullet(doc, "TreeExplainer and KernelExplainer compute Shapley values for all tabular features and fused latent dimensions. The system generates global feature importance bar charts and local force plots explaining individual woreda forecasts (e.g., 'Babile Woreda assigned High Drought Risk: +38% due to 60-day rainfall deficit, +22% due to low SMAP root-zone moisture, -8% mitigated by high soil clay water retention').", bold_prefix="Tabular & Multimodal SHAP Attributions: ")
    add_bullet(doc, "Visualizes spatial activation maps from the final convolutional layer of the ResNet branch. The heatmaps overlay satellite true-color imagery to highlight specific microclimatic zones (e.g., degraded slope catchments vs. riparian valleys) driving the model's visual predictions.", bold_prefix="Spatial Grad-CAM Saliency: ")
    add_bullet(doc, "Permutation feature importance and temporal attention scores quantify the relative contribution of each antecedent month, identifying whether the shock is driven by acute recent failure (Lead 1) or cumulative multi-season deficit (Leads 2–6).", bold_prefix="Temporal Sequence Attribution: ")

    # 3.9 Knowledge Graph
    add_heading_2(doc, "3.9 Neo4j Semantic Knowledge Graph Architecture")
    add_body(doc, "A graph database (Neo4j 5.x) explicitly models the semantic entities and cascading dependencies of Eastern Hararghe's agricultural landscape. The graph schema comprises:")
    add_bullet(doc, "Woreda, Kebele, ClimateRecord, VegetationRecord, SoilMoistureRecord, Crop, LivestockSystem, DroughtEvent, FoodInsecurityStatus, VulnerablePopulation, EarlyWarningAlert, and ReliefProgram.", bold_prefix="Core Entity Nodes: ")
    add_bullet(doc, "HAS_CLIMATE, HAS_VEGETATION, HAS_SOIL_MOISTURE, CULTIVATES_CROP, EXPERIENCES_DROUGHT, SUFFERS_FOOD_INSECURITY, AFFECTS_LIVELIHOOD, TRIGGERS_ALERT, and MITIGATED_BY.", bold_prefix="Semantic Relationships: ")

    add_body(doc, "Sample Cypher Analytical Query for Cascading Vulnerability Reasoning:")
    add_callout(doc,
        "MATCH (w:Woreda)-[:EXPERIENCES_DROUGHT]->(d:DroughtEvent)\n"
        "MATCH (w)-[:CULTIVATES_CROP]->(c:Crop {name: 'Maize'})\n"
        "MATCH (w)-[:SUFFERS_FOOD_INSECURITY]->(f:FoodInsecurityStatus)\n"
        "WHERE d.severity IN ['Severe', 'Extreme'] AND f.ipc_phase >= 3\n"
        "RETURN w.name AS HighRiskWoreda, d.spi3 AS MoistureDeficit, c.vulnerability AS CropExposure,\n"
        "       f.ipc_phase AS CrisisPhase, f.affected_population AS PopulationAtRisk\n"
        "ORDER BY f.ipc_phase DESC, d.spi3 ASC;",
        title="NEO4J CYPHER QUERY: MULTI-HAZARD VULNERABILITY REASONING", alert_type="info"
    )

    # 3.10 Experimental Design
    add_heading_2(doc, "3.10 Experimental Design, Validation Protocols and the 'Honest Lead Horizon'")
    add_body(doc, "To ensure uncompromising scientific validity and eliminate data leakage, this study enforces strict chronological out-of-sample partitioning:")
    add_bullet(doc, "January 2015 – December 2021 (7 years). All feature scalers, normalizers, and model weights are fitted exclusively on this historical window.", bold_prefix="1. Model Training Window: ")
    add_bullet(doc, "January 2022 – December 2023 (2 years). Used for hyperparameter tuning, dropout optimization, early stopping, and fusion cross-attention calibration.", bold_prefix="2. Out-of-Sample Validation Window: ")
    add_bullet(doc, "January 2024 – December 2026 (3 years). Completely held-out testing window containing recent historic droughts. Evaluated without updating model weights.", bold_prefix="3. Independent Out-of-Sample Hindcasting Test Window: ")

    add_heading_3(doc, "3.10.1 The 'Honest Lead Horizon' Principle")
    add_body(doc, "In agricultural early warning, issuing false certainty at distant forecast horizons can induce catastrophic misinvestments by smallholder farmers. Each forecast lead (1, 2, 3 months ahead) is rigorously evaluated against local climatology using the Brier Skill Score (BSS):")
    add_body(doc, "BSS = 1 - [Brier_{model} / Brier_{climatology}]\nWhere Brier is the mean squared probability error. A positive BSS demonstrates genuine predictive superiority over historical climatological odds. If BSS <= 0 at distant leads, the system enforces a strict dual-track reporting policy: Lead 1 is published as a high-resolution quantitative probability map, while Leads 2 and 3 are published solely as qualitative directional outlooks accompanied by transparent skill indicators.")

    add_heading_3(doc, "3.10.2 Evaluation Metrics & Class Imbalance Handling")
    add_body(doc, "Severe drought and acute food insecurity events are inherently rare, causing extreme class imbalance (e.g., IPC Phase 4/5 representing <10% of historical woreda-months). Relying on raw classification accuracy introduces catastrophic bias. Model performance is comprehensively evaluated using:")
    add_bullet(doc, "Precision, Recall (Probability of Detection [POD]), Macro-averaged F1-Score, Receiver Operating Characteristic Area Under Curve (ROC-AUC), and Precision-Recall Area Under Curve (PR-AUC).")
    add_bullet(doc, "Continuous error metrics: Root Mean Square Error (RMSE) and Mean Absolute Error (MAE) for continuous Sc-PDSI and SPI predictions.")
    add_bullet(doc, "Probabilistic calibration: Brier Skill Score (BSS) and Reliability Calibration Diagrams assessing whether predicted probabilities reflect observed empirical frequencies.")
    add_bullet(doc, "Class Imbalance Mitigation: Focal Loss with focusing parameter γ = 2.0 to down-weight easy negative examples, paired with class-weighted cross-entropy loss. Synthetic Minority Over-sampling Technique (SMOTE) is applied strictly within training folds only.")

    # 3.11 Software Architecture
    add_heading_2(doc, "3.11 Software Engineering, Deployment Architecture and User Delivery")
    add_body(doc, "AgriMinds / Hararghe AgroAlert AI is constructed as a production-grade, cloud-native enterprise system designed for high concurrency, military-grade security, and offline resilience:")
    add_bullet(doc, "Engineered with Python 3.12, FastAPI, and async SQLAlchemy 2. Employs Pydantic v2 schemas for strict OpenAPI 3.1 contracts. Shared TypeScript types (@agriminds/api-types) prevent schema drift across web and mobile clients.", bold_prefix="Backend Microservice Core: ")
    add_bullet(doc, "Passwords encrypted with Argon2id (19 MiB memory cost, 2 iterations). Sign-in uses constant-time comparisons with 15-minute account lockout after 8 failed attempts. 15-minute JWT access tokens paired with 14-day rotating SHA-256 refresh tokens with automatic theft revocation.", bold_prefix="Multi-Tier Security & Authentication: ")
    add_bullet(doc, "PostgreSQL 17 enforces relational foreign keys across woredas, accounts, farm plots, and advisory audit logs. A decoupled Star Schema (analytics schema: dim_woreda, dim_crop, fact_farm, fact_advisory, fact_risk) is queried by read-only user agriminds_bi, powering embedded self-hosted Metabase BI dashboards without commercial licensing.", bold_prefix="Relational Schema & Analytics Star Schema: ")
    add_bullet(doc, "Built with Next.js 16 (App Router), React 19, and Tailwind CSS v4. Features role-scoped tenancy: Ministers view watershed-wide choropleths and risk exposure (/ministry); Development Agents are scoped strictly to their woreda; Farmers view plot risk badges, advisory recommendations, and 'Confirm Read' buttons (/farm).", bold_prefix="Web Command Centre: ")
    add_bullet(doc, "Built with Expo / React Native, persisted to AsyncStorage via TanStack Query. Caches grids and advisories for full offline operation in remote kebeles. Features an ergonomic 9-key ThumbPad on-screen directional keypad for one-handed field navigation. Fully localized in English, Amharic, and Afaan Oromoo.", bold_prefix="Offline-First Mobile Field Application: ")
    add_bullet(doc, "Standardized Makefile automation: 'make up' (starts Docker Compose stack), 'make ingest' (downloads public datasets), 'make train' (executes full deep learning pipeline), 'make test' (runs pytest and Vitest suites).", bold_prefix="Operational Runbook & DevOps: ")

    # 3.12 Ethical Governance
    add_heading_2(doc, "3.12 Ethical Considerations, Data Governance and Reproducibility Protocols")
    add_body(doc, "The research adheres to strict ethical and operational standards:")
    add_bullet(doc, "All spatial data utilized are anonymized and aggregated to woreda administrative levels or 8×8 topographic grid cells. No personally identifiable smallholder information is stored or exposed.")
    add_bullet(doc, "The system strictly enforces a human-in-the-loop decision paradigm. Model outputs are explicitly communicated as decision-support evidence; they never trigger automated relief actions or override statutory human authority.")
    add_bullet(doc, "Model explanations (SHAP / Grad-CAM) identify empirical associations rather than absolute causal certainty, preventing unwarranted conclusions.")
    add_bullet(doc, "All software repositories, Docker containers, training seeds, and feature pipelines are version-controlled under an open-source MIT license, ensuring zero-barrier academic reproducibility.")

    doc.add_page_break()

print("Chapter 3 module defined.")
