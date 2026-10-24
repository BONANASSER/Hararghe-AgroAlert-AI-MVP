"""
build_chapter_4_5_appendices.py
Chapter 4: Work Plan, Resource Requirements & Deliverables
Chapter 5: Academic References
Appendices A, B, C, D, E
"""

import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from build_master_concept_note import (
    add_heading_1, add_heading_2, add_heading_3, add_body, add_bullet, 
    add_callout, style_table, HEX_PRIMARY, HEX_SECONDARY, HEX_CALLOUT_BG
)

def build_chapter_4_5_appendices(doc):
    # CHAPTER 4
    add_heading_1(doc, "CHAPTER FOUR: WORK PLAN, RESOURCE REQUIREMENTS AND DELIVERABLES")
    
    # 4.1 Work Plan
    add_heading_2(doc, "4.1 Chronological Research Schedule and Milestone Gantt Chart")
    add_body(doc, "The proposed master's research is structured across a rigorous 12-month execution lifecycle organized into six discrete, interdependent work packages (WPs) spanning from conceptualization to thesis defense:")

    wp_headers = ["Work Package (WP)", "Major Research Activities & Computational Milestones", "Time Horizon (Months)", "Verifiable Output / Milestone"]
    wp_widths = [Inches(1.4), Inches(2.5), Inches(1.1), Inches(1.5)]
    wp_data = [
        ["WP1: Literature Review & Design", "Theoretical formulation, parameter bounding, ethics clearance, and conceptual architecture refinement.", "Months 1–2", "Approved research concept note & formal literature synthesis dossier"],
        ["WP2: Data Ingestion & Harmonization", "Automated connectors for NOAA, CHIRPS, SMAP, MODIS, ERA5, SoilGrids, and FEWS NET; SHA-256 manifest system.", "Months 3–4", "Standardized Woreda × Month master data cube with cryptographic checksums"],
        ["WP3: Deep Learning & Benchmarking", "Conv1D-LSTM ENSO model; ResNet-50 patch encoder; LSTM temporal branch; FFT harmonic branch; Gated Fusion engine.", "Months 5–6", "Trained model checkpoints and comparative empirical benchmark tables"],
        ["WP4: Decision Support, IEK & XAI", "Crop sensitivity multipliers (s); 4-tier prescriptive matrix; IEK consensus engine; SHAP, Grad-CAM, Neo4j graph.", "Months 7–8", "Interpretable advisory engine, XAI saliency visualizers, populated Neo4j database"],
        ["WP5: Software & Cloud Deployment", "FastAPI async microservice, PostgreSQL 17 Star Schema, Next.js 16 Web Command Centre, Expo offline mobile app.", "Months 9–10", "Production-grade cloud-hosted prototype and containerized Docker images"],
        ["WP6: Evaluation & Defense", "Independent out-of-sample hindcasting (2024–2026), BSS gating, thesis manuscript writing, and final defense.", "Months 11–12", "Completed MSc thesis, peer-reviewed manuscript submission, successful defense"]
    ]
    tbl_wp = doc.add_table(rows=1, cols=4)
    style_table(tbl_wp, wp_widths, wp_headers, wp_data)

    # 4.2 Resource Requirements
    add_heading_2(doc, "4.2 Computational, Hardware and Software Resource Requirements")
    add_bullet(doc, "NVIDIA RTX 4090 / A100 GPU workstation (or Google Cloud Platform / Colab Pro enterprise instances) equipped with 32 GB+ VRAM, 64 GB system RAM, and 2 TB high-speed NVMe storage for processing multi-spectral satellite rasters.", bold_prefix="Hardware & High-Performance Computing: ")
    add_bullet(doc, "Python 3.12, PyTorch 2.4, Torchvision, Scipy, Scikit-learn, GDAL, Rasterio, GeoPandas, Xarray, NetCDF4, SHAP, and Grad-CAM for machine learning and geospatial engineering.", bold_prefix="Scientific & ML Software Stack: ")
    add_bullet(doc, "FastAPI, Pydantic v2, SQLAlchemy 2 (async), Alembic, PostgreSQL 17, PostGIS, Redis 7, Neo4j 5.x Graph Database, and Metabase Business Intelligence.", bold_prefix="Backend & Database Ecosystem: ")
    add_bullet(doc, "Next.js 16 (App Router), React 19, Tailwind CSS v4, Lucide Icons, Expo / React Native, TanStack Query, and AsyncStorage for multi-platform client delivery.", bold_prefix="Web & Mobile Frameworks: ")

    # 4.3 Expected Deliverables
    add_heading_2(doc, "4.3 Expected Scientific and Practical Deliverables")
    add_bullet(doc, "A finalized, rigorously defended Master of Science thesis manuscript in Data Science fulfilling all academic criteria of Haramaya University.", bold_prefix="1. Master of Science Thesis: ")
    add_bullet(doc, "At least two peer-reviewed academic manuscripts submitted to high-impact international journals (e.g., Agricultural and Forest Meteorology, Remote Sensing of Environment, or Climate Services).", bold_prefix="2. High-Impact Publications: ")
    add_bullet(doc, "A production-grade, containerized Docker repository on GitHub with complete CI/CD automation, open-access manifests, and reproducible training runbooks.", bold_prefix="3. Open-Source Codebase: ")
    add_bullet(doc, "A live, cloud-deployed decision support platform (Next.js Web Command Centre + Expo offline mobile application) bridging predictive intelligence to agricultural extension personnel.", bold_prefix="4. Operational Decision Platform: ")

    # 4.4 Risk Assessment
    add_heading_2(doc, "4.4 Risk Management and Mitigation Framework")
    risk_headers = ["Identified Research Risk", "Severity & Likelihood", "Concrete Technical & Operational Mitigation Strategy"]
    risk_widths = [Inches(1.8), Inches(1.5), Inches(3.2)]
    risk_data = [
        ["Severe cloud contamination in optical MODIS imagery during peak Kiremt rains", "High / High", "Integrate microwave SMAP soil moisture and ERA5 surface reanalysis, which penetrate heavy cloud cover, paired with temporal Savitzky-Golay filtering."],
        ["Limited or delayed woreda-level acute food insecurity labels from official agencies", "High / Medium", "Restrict supervised food-security classification strictly to verified 2020–2026 FEWS NET shapefiles; utilize physical Sc-PDSI/SPI for full 2015–2026 window."],
        ["Computational memory overflow when processing high-resolution spatial patches", "Medium / Medium", "Employ gradient accumulation, mixed-precision (FP16) training, and memory-mapped HDF5 data loaders to bound GPU VRAM usage."],
        ["Low advisory adoption by rural farmers due to cultural skepticism of AI models", "High / Medium", "Deploy the Bi-Directional IEK Consensus Engine and trilingual offline mobile app, actively engaging community elders and local kebele development agents."]
    ]
    tbl_risk = doc.add_table(rows=1, cols=3)
    style_table(tbl_risk, risk_widths, risk_headers, risk_data)

    doc.add_page_break()

    # CHAPTER 5: REFERENCES
    add_heading_1(doc, "CHAPTER FIVE: ACADEMIC REFERENCES AND BIBLIOGRAPHY")
    
    references = [
        "Abate, J., Aman, A., & Adem, D. (2025). Integration of satellite data for predicting crop yields in Eastern Ethiopia using machine learning. Scientific Reports, 15(1), 33809. https://doi.org/10.1038/s41598-025-00810-z",
        "Abate, M., Tadesse, T., & Bewket, W. (2025). Climate variability, drought dynamics, and rural livelihood vulnerability in the Choke Mountain Watershed, Upper Blue Nile Basin, Ethiopia. Journal of Arid Environments, 218, 105022. https://doi.org/10.1016/j.jaridenv.2024.105022",
        "Arash, K., Wondie, M., & Belayneh, E. (2025). Deep learning frameworks for hydro-climatic forecasting in mountainous watersheds: Coupling CNNs and LSTMs for teleconnection modeling. Water Resources Research, 61(4), e2024WR036512. https://doi.org/10.1029/2024WR036512",
        "Baye, Z. D., Assabie, Y., & Asfaw, T. T. (2026). Predicting food security in Ethiopia using spatiotemporal integration of heterogeneous data. Journal of Agriculture and Food Research, 26, 102674. https://doi.org/10.1016/j.jafr.2026.102674",
        "Busker, T., van den Hurk, B., de Moel, H., van den Homberg, M., van Straaten, C., Odongo, R. A., & Aerts, J. C. J. H. (2024). Predicting food-security crises in the Horn of Africa using machine learning. Earth's Future, 12(8), e2023EF004211. https://doi.org/10.1029/2023EF004211",
        "FEWS NET. (2025). East Africa Alert: Historic dry rainy season triggers alarm for deepening food insecurity across the eastern Horn of Africa. Famine Early Warning Systems Network. https://fews.net/east-africa/alert/december-2025-0",
        "Funk, C., Peterson, P., Landsfeld, M., Pedreros, D., Verdin, J., Shukla, S., Husak, G., Rowland, J., Harrison, L., Hoell, A., & Michaelsen, J. (2026). The Climate Hazards center InfraRed Precipitation with Station data (CHIRPS) version 3. Scientific Data, 13, 718. https://doi.org/10.1038/s41597-026-07096-4",
        "Hochreiter, S., & Schmidhuber, J. (1997). Long short-term memory. Neural Computation, 9(8), 1735–1780. https://doi.org/10.1162/neco.1997.9.8.1735",
        "Integrated Food Security Phase Classification (IPC). (2023). Technical Manual Version 3.1: Evidence and Standards for Better Food Security and Nutrition Decisions. IPC Global Strategic Programme. Rome: FAO.",
        "ISRIC – World Soil Information. (2020). SoilGrids250m 2.0: Global gridded soil information based on machine learning. https://soilgrids.org/",
        "Lin, T. Y., Goyal, P., Girshick, R., He, K., & Dollár, P. (2017). Focal loss for dense object detection. IEEE Transactions on Pattern Analysis and Machine Intelligence, 42(2), 318–327.",
        "Lundberg, S. M., & Lee, S. I. (2017). A unified approach to interpreting model predictions. Advances in Neural Information Processing Systems (NeurIPS 2017), 30, 4765–4774.",
        "McKee, T. B., Doesken, N. J., & Kleist, J. (1993). The relationship of drought frequency and duration to time scales. Proceedings of the 8th Conference on Applied Climatology, 17(22), 179–183.",
        "Megbar, W., & Tadesse, T. (2016). Teleconnection of El Niño–Southern Oscillation with seasonal rainfall and drought patterns over the Amhara Regional State, Ethiopia. International Journal of Climatology, 36(11), 3845–3858. https://doi.org/10.1002/joc.4600",
        "Menberu, T., & Addisu, S. (2018). Spatial and temporal evaluation of agricultural drought using the Self-Calibrated Palmer Drought Severity Index (Sc-PDSI) in the Upper Blue Nile River Basin. Theoretical and Applied Climatology, 134(3), 1145–1159. https://doi.org/10.1007/s00704-017-2336-0",
        "Palmer, W. C. (1965). Meteorological Drought. Research Paper No. 45. Washington, D.C.: U.S. Department of Commerce Weather Bureau.",
        "Selvaraju, R. R., Cogswell, M., Das, A., Vedantam, R., Parikh, D., & Batra, D. (2017). Grad-CAM: Visual explanations from deep networks via gradient-based localization. Proceedings of the IEEE International Conference on Computer Vision (ICCV), 618–626. https://doi.org/10.1109/ICCV.2017.74",
        "Shamsuddin, A. K., Rahman, M. A., & Khan, S. (2024). Multimodal deep learning integration of image, weather, and phenotypic data under temporal effects for early prediction of maize yield. Remote Sensing, 16(21), 4043. https://doi.org/10.3390/rs16214043",
        "Taklu, T., Simane, B., & Zaitchik, B. (2023). Bridging the gap between seasonal climate forecasts and smallholder farmer decisions in Ethiopia: The role of Indigenous Ecological Knowledge. Climate Services, 30, 100356. https://doi.org/10.1016/j.cliser.2023.100356",
        "Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). Attention is all you need. Advances in Neural Information Processing Systems (NeurIPS 2017), 30, 5998–6008.",
        "Wells, N., Goddard, S., & Hayes, M. J. (2004). A Self-Calibrating Palmer Drought Severity Index. Journal of Climate, 17(12), 2335–2351. https://doi.org/10.1175/1520-0442(2004)017<2335:ASPDSI>2.0.CO;2",
        "WorldPop. (2022). Global High Resolution Population Denominators Project. University of Southampton. https://hub.worldpop.org/",
        "Yao, X., Zhang, Y., & Liu, Q. (2024). Multimodal deep learning-based drought monitoring research for winter wheat during critical growth stages. PLOS ONE, 19(4), e0300746. https://doi.org/10.1371/journal.pone.0300746"
    ]
    for ref in references:
        add_body(doc, ref, space_after=4)

    doc.add_page_break()

    # APPENDICES
    add_heading_1(doc, "APPENDICES")
    
    # Appendix A
    add_heading_2(doc, "Appendix A: Master Analytical Dataset Schema and Data Dictionary")
    add_body(doc, "The master analytical dataset is structured as a Woreda × Month panel data cube. The standardized schema is detailed in Table A.1:")

    app_a_headers = ["Field Name", "Data Type", "Measurement Unit", "Primary Data Source", "Description & Analytical Role"]
    app_a_widths = [Inches(1.5), Inches(0.9), Inches(1.1), Inches(1.3), Inches(1.7)]
    app_a_data = [
        ["woreda_id", "String", "Categorical P-Code", "ESS / Oromia Admin", "Unique administrative identifier for target woreda"],
        ["woreda_name", "String", "Text", "ESS / Oromia Admin", "Official administrative name (e.g., Babile, Fedis, Deder)"],
        ["timestamp", "Date", "YYYY-MM-01", "Pipeline Clock", "Target calendar observation month"],
        ["chirps_precip", "Float", "mm / month", "CHIRPS v3", "Cumulative monthly rainfall total"],
        ["precip_anomaly", "Float", "Standard Deviations", "Derived (30-yr baseline)", "Monthly rainfall departure from long-term normal"],
        ["spi_1m", "Float", "Z-Score", "Derived Gamma Fit", "1-month Standardized Precipitation Index"],
        ["spi_3m", "Float", "Z-Score", "Derived Gamma Fit", "3-month Standardized Precipitation Index (Root-zone stress)"],
        ["spi_6m", "Float", "Z-Score", "Derived Gamma Fit", "6-month Standardized Precipitation Index (Hydrological)"],
        ["sc_pdsi", "Float", "Palmer Scale (-4 to +4)", "Derived Water Balance", "Two-layer Self-Calibrated Palmer Drought Severity Index"],
        ["smap_soil_moist", "Float", "m³ / m³", "NASA SMAP L3", "Mean surface soil moisture content (0–5 cm)"],
        ["sm_anomaly", "Float", "Standard Deviations", "Derived SMAP normal", "Soil moisture departure from historical seasonal mean"],
        ["modis_ndvi", "Float", "Index (-1.0 to +1.0)", "MODIS MOD13Q1", "Mean Normalized Difference Vegetation Index greenness"],
        ["modis_evi", "Float", "Index (-1.0 to +1.0)", "MODIS MOD13Q1", "Enhanced Vegetation Index (atmospheric-resistant)"],
        ["vci", "Float", "Percentage (0–100%)", "Derived MODIS extremes", "Vegetation Condition Index relative to historical envelope"],
        ["lst_day", "Float", "Kelvin / Celsius", "MODIS MOD11A2", "Daytime Land Surface Temperature (thermal stress)"],
        ["lst_anomaly", "Float", "Celsius departure", "Derived MOD11A2 normal", "Thermal anomaly indicating evaporative stress"],
        ["t2m_era5", "Float", "Celsius", "ECMWF ERA5", "2-meter mean air temperature"],
        ["u10_wind, v10_wind", "Float", "m / s", "ECMWF ERA5", "Zonal and meridional 10 m atmospheric wind components"],
        ["nino34_anomaly", "Float", "Celsius departure", "NOAA PSL ERSSTv6", "Equatorial Pacific Niño 3.4 SST anomaly (Teleconnection)"],
        ["soil_awc", "Float", "mm / profile", "ISRIC SoilGrids", "Available Water Capacity of total soil profile (AWC)"],
        ["soil_clay_pct", "Float", "Percentage (0–100%)", "ISRIC SoilGrids", "Clay content fraction governing water holding capacity"],
        ["population_density", "Float", "Persons / km²", "WorldPop", "Demographic density and population exposure"],
        ["crop_type", "String", "Categorical", "CSA / Agriculture Office", "Primary staple crop cultivated on monitored plot"],
        ["fews_ipc_phase", "Integer", "Discrete (1 to 5)", "FEWS NET / IPC", "Supervised acute food insecurity classification target"],
        ["data_manifest_sha256", "String", "Hex Hash", "Manifest System", "Cryptographic integrity verification checksum"]
    ]
    tbl_app_a = doc.add_table(rows=1, cols=5)
    style_table(tbl_app_a, app_a_widths, app_a_headers, app_a_data)

    # Appendix B
    add_heading_2(doc, "Appendix B: Mathematical Formulations of Deep Learning Operations")
    add_callout(doc,
        "1. Multi-Head Cross-Attention Formulation:\n"
        "Given Query Q derived from Temporal Sequence embedding e_temporal, and Key K, Value V derived from Spatial Patch embedding e_spatial and Tabular embedding e_tabular:\n"
        "Attention(Q, K, V) = softmax[(Q * K^T) / sqrt(d_k)] * V\n"
        "MultiHead(Q, K, V) = Concat(head_1, ..., head_h) * W_O\n"
        "where head_i = Attention(Q * W_i^Q, K * W_i^K, V * W_i^V)\n\n"
        "2. Focal Loss for Extreme Class Imbalance:\n"
        "FL(p_t) = -α_t * (1 - p_t)^γ * log(p_t)\n"
        "where p_t is the model's estimated probability for the ground-truth class, α_t balances class frequencies, and γ = 2.0 smoothly reduces the loss contribution from easy negative examples, focusing training on rare severe drought (IPC Phase 4/5) events.\n\n"
        "3. Brier Skill Score (BSS) for 'Honest Lead Horizon' Gating:\n"
        "BS = (1 / N) * Σ (f_n - o_n)^2\n"
        "BSS = 1 - [BS_{model} / BS_{climatology}]\n"
        "where f_n is the forecast probability, o_n in {0, 1} is observed occurrence, and BS_{climatology} is the Brier score of long-term historical base rates.",
        title="MATHEMATICAL FORMULATIONS: CROSS-ATTENTION, FOCAL LOSS & BRIER SKILL SCORE", alert_type="info"
    )

    # Appendix C
    add_heading_2(doc, "Appendix C: Comprehensive 14-Experiment Baseline & Ablation Matrix")
    add_body(doc, "To rigorously quantify the empirical value of multimodal hybridization, 14 systematically designed baseline and ablation experiments will be executed under identical chronological splits:")

    app_c_headers = ["Exp ID", "Model Family / Architecture", "Input Modalities Evaluated", "Primary Scientific Objective"]
    app_c_widths = [Inches(0.8), Inches(1.8), Inches(2.2), Inches(1.7)]
    app_c_data = [
        ["E01", "Logistic Regression Baseline", "Tabular environmental aggregates only", "Establish simple linear classification benchmark"],
        ["E02", "Random Forest Classifier", "Tabular environmental + socioeconomic features", "Non-linear tree ensemble tabular benchmark"],
        ["E03", "XGBoost Classifier", "All engineered tabular features + anomalies", "State-of-the-art gradient boosted tree tabular baseline"],
        ["E04", "Dynamical RCM Baseline", "Regional Climate Model numerical precipitation", "Compare against conventional meteorological physics"],
        ["E05", "Unimodal Spatial 2D-CNN", "MODIS multi-spectral satellite rasters only", "Isolate predictive skill of visual spatial texture"],
        ["E06", "Unimodal Recurrent LSTM", "Sequential hydro-climatic time series only", "Isolate predictive skill of sequential temporal memory"],
        ["E07", "Conv1D-LSTM ENSO Alone", "Equatorial Pacific SST anomalies only", "Measure skill of remote global teleconnection alone"],
        ["E08", "Dual Fusion: CNN + LSTM", "Satellite patches + temporal climate series", "Evaluate conventional spatiotemporal coupling"],
        ["E09", "Tri-Branch: CNN+LSTM+MLP", "Satellite patches + climate series + tabular socio", "Assess addition of structured socioeconomic data"],
        ["E10", "Super-Hybrid (Proposed)", "CNN + LSTM + FFT + MLP + Cross-Attention", "Full proposed architecture with harmonic FFT & attention"],
        ["E11", "Lead Horizon: Lead 1", "Full Super-Hybrid at 1-month lead", "Assess immediate lead predictive skill and BSS"],
        ["E12", "Lead Horizon: Lead 2", "Full Super-Hybrid at 2-month lead", "Assess medium-range lead predictive skill and BSS"],
        ["E13", "Lead Horizon: Lead 3", "Full Super-Hybrid at 3-month lead", "Assess seasonal lead predictive skill and BSS gating"],
        ["E14", "Spatial Holdout Validation", "Full Super-Hybrid evaluated on held-out woredas", "Verify spatial generalization across unseen topography"]
    ]
    tbl_app_c = doc.add_table(rows=1, cols=4)
    style_table(tbl_app_c, app_c_widths, app_c_headers, app_c_data)

    # Appendix D
    add_heading_2(doc, "Appendix D: Neo4j Knowledge Graph Cypher Schema & Cascading Query Examples")
    add_callout(doc,
        "// Cypher Query: Identify Woredas experiencing compounded Drought & Food Insecurity\n"
        "// with vulnerable sorghum or maize crops, returning population at risk\n\n"
        "MATCH (w:Woreda)-[:LOCATED_IN]->(z:Zone {name: 'East Hararghe'})\n"
        "MATCH (w)-[:EXPERIENCES_DROUGHT]->(d:DroughtEvent {season: 'Belg 2026'})\n"
        "MATCH (w)-[:CULTIVATES_CROP]->(c:Crop)\n"
        "MATCH (w)-[:HAS_POPULATION]->(p:VulnerablePopulation)\n"
        "MATCH (w)-[:SUFFERS_FOOD_INSECURITY]->(f:FoodInsecurityStatus)\n"
        "WHERE d.spi3 <= -1.5 AND c.name IN ['Maize', 'Sorghum'] AND f.ipc_phase >= 3\n"
        "RETURN w.name AS WoredaName, \n"
        "       d.spi3 AS SPI3_DroughtSeverity, \n"
        "       c.name AS VulnerableCrop, \n"
        "       f.ipc_phase AS IPC_CrisisPhase,\n"
        "       p.total_count AS ExposedPopulation,\n"
        "       [(w)-[:RECEIVES_ALERT]->(a:EarlyWarningAlert) | a.action_package] AS PrescriptiveAdvisories\n"
        "ORDER BY d.spi3 ASC, f.ipc_phase DESC;",
        title="NEO4J CYPHER QUERY: COMPOUNDED MULTI-HAZARD RISK RETRIEVAL", alert_type="info"
    )

    # Appendix E
    add_heading_2(doc, "Appendix E: Multi-Tier API Endpoint Specification and UI Architecture")
    add_body(doc, "The cloud-native backend microservice exposes a fully typed RESTful OpenAPI 3.1 specification under /api/v1. Key endpoints governing early warning and advisory evaluation include:")

    app_e_headers = ["HTTP Method", "API Endpoint Path", "Access Role", "Operational Functional Purpose"]
    app_e_widths = [Inches(1.1), Inches(2.0), Inches(1.3), Inches(2.1)]
    app_e_data = [
        ["GET", "/api/v1/health/ready", "Public", "Service readiness probe; returns 200 only when model weights and database pool are loaded."],
        ["POST", "/api/v1/auth/login", "Public", "Argon2id authentication; returns 15-min JWT access token & sets rotating refresh token cookie."],
        ["GET", "/api/v1/drought/map", "Signed-in", "Serves woreda-level drought hazard probability map P(SPI-3<=-1) for the requested lead."],
        ["GET", "/api/v1/drought/cell", "Signed-in", "Retrieves high-resolution 8×8 grid cell climatological history and forecast by row/col or GPS."],
        ["POST", "/api/v1/advisories/evaluate", "Signed-in", "Evaluates plot crop sensitivity (s), adjusted risk P_adj, and triggers IEK consensus check."],
        ["GET", "/api/v1/food-security/forecast", "Signed-in", "Emits FEWS NET IPC phase probability distribution across target woredas."],
        ["GET", "/api/v1/enso/outlook", "Signed-in", "Retrieves Niño 3.4 SST history and multi-lead Conv1D-LSTM forecasts with skill metrics."],
        ["GET", "/api/v1/xai/attributions", "Signed-in", "Returns SHAP waterfall attributions and Grad-CAM image overlay coordinates for a woreda."],
        ["GET", "/api/v1/analytics/metabase", "Ministers / Admins", "Generates signed embed URL for zero-license Metabase Business Intelligence dashboards."]
    ]
    tbl_app_e = doc.add_table(rows=1, cols=4)
    style_table(tbl_app_e, app_e_widths, app_e_headers, app_e_data)

    add_body(doc, "The multi-platform UI architecture enforces role-scoped access control:")
    add_bullet(doc, "Displays zone-wide comparative choropleth maps, aggregate exposure percentages (Moderate, High, Severe), woreda-by-woreda vulnerability matrices, crop mix distributions, and real-time advisory delivery read-receipt rates.", bold_prefix="Ministry Command Dashboard (/ministry): ")
    add_bullet(doc, "Optimized for rural extension agents, displaying assigned kebele farm plots, plot-specific crop sensitivity risk badges, 4-tier prescriptive agronomic actions, and the IEK traditional indicator submission form.", bold_prefix="Development Agent & Farmer Action Portal (/farm): ")
    add_bullet(doc, "Visualizes Brier Skill Scores, ROC-AUC curves, and comparative benchmark tables across forecast leads 1 to 12, enforcing transparency regarding the 'Honest Lead Horizon'.", bold_prefix="Forecast Horizon & Validation Metrics Portal (/prediction/metrics): ")

print("Chapter 4, 5, and Appendices module defined.")
