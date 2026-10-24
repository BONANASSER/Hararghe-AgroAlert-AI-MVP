"""
generate_concept_note_docx.py
Modular, robust script that compiles the complete MSc Thesis Concept Note into a styled .docx file.
"""

import sys
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

from build_master_concept_note import (
    create_document, add_title, add_subtitle, add_heading_1, add_heading_2, 
    add_heading_3, add_body, add_bullet, add_callout, style_table,
    set_cell_background, set_cell_margins, set_table_borders,
    HEX_PRIMARY, HEX_SECONDARY, HEX_ACCENT, HEX_DARK, HEX_LIGHT_BG, HEX_CALLOUT_BG, HEX_BORDER
)

def build_front_matter(doc):
    # Header Info
    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_inst.paragraph_format.space_before = Pt(0)
    p_inst.paragraph_format.space_after = Pt(2)
    r = p_inst.add_run("HARAMAYA UNIVERSITY\nPOSTGRADUATE PROGRAM DIRECTORATE\nCOLLEGE OF COMPUTING AND INFORMATICS\nDEPARTMENT OF INFORMATION SCIENCE")
    r.font.name = "Arial"
    r.font.size = Pt(11)
    r.font.bold = True
    r.font.color.rgb = RGBColor(26, 54, 93)

    p_prog = doc.add_paragraph()
    p_prog.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_prog.paragraph_format.space_before = Pt(4)
    p_prog.paragraph_format.space_after = Pt(24)
    r_prog = p_prog.add_run("MASTER OF SCIENCE IN DATA SCIENCE PROGRAM")
    r_prog.font.name = "Arial"
    r_prog.font.size = Pt(12)
    r_prog.font.bold = True
    r_prog.font.color.rgb = RGBColor(43, 108, 176)

    # Title
    add_title(doc, "AI-BASED MULTIMODAL DEEP LEARNING EARLY WARNING SYSTEM FOR DROUGHT, CROP ADVISORY, AND FOOD INSECURITY PREDICTION USING SATELLITE IMAGERY, CLIMATE, VEGETATION, SOCIOECONOMIC, AND AGRICULTURAL DATA IN EASTERN ETHIOPIA")
    add_subtitle(doc, "A Super-Hybrid Spatiotemporal Deep Learning Framework Integrating Atmospheric Teleconnections, Crop Sensitivity Phenology, Explainable AI, Knowledge Graphs, and Indigenous Ecological Knowledge")

    # Metadata Table
    meta_headers = ["Parameter / Dimension", "Thesis Specification"]
    meta_widths = [Inches(2.3), Inches(4.2)]
    meta_data = [
        ["Researcher / Principal Investigator", "Bona Nasser Abdo (BSc, Graduate Researcher)"],
        ["Academic Program", "Master of Science (MSc) in Data Science"],
        ["Department & College", "Department of Information Science | College of Computing and Informatics"],
        ["Host Institution", "Haramaya University, Haramaya, Ethiopia"],
        ["Target Geographic Scope", "Eastern and Western Hararghe Zones (East & West Hararge, Oromia Regional State)"],
        ["Primary Spatial Unit", "Woreda Level (Admin 3: 41 Woredas) & Catchment Grids"],
        ["Core Integrated Modeling Window", "1990 to October 2026 (Continuous Multi-Decadal Panel: 18,122 Woreda-Months)"],
        ["Target Forecast Horizons", "Lead 1 (1 Month, Quantitative Probability Map); Leads 2–3 (Multi-Lead Seasonal Outlooks)"],
        ["Core Methodological Paradigms", "Super-Hybrid CNN-LSTM-Fourier Deep Learning, Multimodal Cross-Attention Fusion, Sc-PDSI Climatology"],
        ["Applied Decision-Support Layer", "Hararghe AgroAlert AI / AgriMinds Enterprise Decision Platform (Web Command + Offline Mobile)"],
        ["Submission Date & Academic Year", "Academic Year 2026/2027 | Haramaya, Ethiopia"]
    ]
    tbl_meta = doc.add_table(rows=1, cols=2)
    style_table(tbl_meta, meta_widths, meta_headers, meta_data)

    doc.add_page_break()

    # Declaration Page
    add_heading_1(doc, "DECLARATION OF ORIGINAL RESEARCH")
    add_body(doc, "I, the undersigned, hereby declare that this thesis concept note titled 'AI-Based Multimodal Deep Learning Early Warning System for Drought, Crop Advisory, and Food Insecurity Prediction Using Satellite Imagery, Climate, Vegetation, Socioeconomic, and Agricultural Data in Eastern Ethiopia' is my original work and has not been submitted previously in part or in full to any other university or institution for the award of any degree, diploma, or academic recognition. All primary data sources, satellite repositories, open-access meteorological products, software frameworks, and published scientific literature cited herein have been rigorously acknowledged in complete conformity with international academic standards and Haramaya University research ethics regulations.")
    
    p_sig = doc.add_paragraph()
    p_sig.paragraph_format.space_before = Pt(18)
    p_sig.paragraph_format.space_after = Pt(24)
    p_sig.add_run("Candidate Name: Bona Nasser Abdo\nSignature: ___________________________\t\tDate: ___________________________").font.name = "Calibri"

    # Approval Sheet
    add_heading_1(doc, "APPROVAL SHEET FOR THESIS CONCEPT NOTE")
    add_body(doc, "This thesis concept note has been submitted for official academic review, defense, and approval with our endorsement as university advisors and examiners:")

    app_headers = ["Role / Designation", "Name & Academic Title", "Signature", "Date"]
    app_widths = [Inches(1.8), Inches(2.2), Inches(1.3), Inches(1.2)]
    app_data = [
        ["Major Advisor", "___________________________________", "____________", "____________"],
        ["Co-Advisor", "___________________________________", "____________", "____________"],
        ["Internal Examiner", "___________________________________", "____________", "____________"],
        ["External Examiner", "___________________________________", "____________", "____________"],
        ["Chairperson, DGC", "___________________________________", "____________", "____________"]
    ]
    tbl_app = doc.add_table(rows=1, cols=4)
    style_table(tbl_app, app_widths, app_headers, app_data)

    doc.add_page_break()

    # Submission Cover Letter
    add_heading_1(doc, "FORMAL SUBMISSION COVER LETTER")
    add_body(doc, "To: The Department Graduate Committee (DGC)\nDepartment of Information Science\nCollege of Computing and Informatics\nHaramaya University, Haramaya, Ethiopia\n\nSubject: Submission of MSc Data Science Thesis Concept Note", bold_prefix="MEMORANDUM\n")
    
    add_body(doc, "I am pleased to submit for formal academic review and supervisory assignment my proposed MSc Data Science thesis concept note, titled 'AI-Based Multimodal Deep Learning Early Warning System for Drought, Crop Advisory, and Food Insecurity Prediction Using Satellite Imagery, Climate, Vegetation, Socioeconomic, and Agricultural Data in Eastern Ethiopia'.")
    
    add_body(doc, "The proposed research addresses the chronic and existential challenge of recurring hydro-climatic shocks in Eastern Hararghe Zone, Oromia, Ethiopia, where escalating climate variability drives catastrophic crop failure and acute food insecurity. By synthesizing the cutting-edge mathematical climatology, oceanic-atmospheric teleconnection modeling, and enterprise delivery engineering of the AgriMinds / AI-DREWS framework with the multimodal deep learning, Explainable AI (SHAP & Grad-CAM), Neo4j Knowledge Graph, and FEWS NET IPC food-security modeling paradigms developed at Haramaya University, this research establishes an unprecedented, end-to-end operational blueprint.")
    
    add_body(doc, "Unlike existing systems that either operate at overly coarse global scales (100–200 km GCMs), suffer from retrospective monitoring bias (reporting damage only after physiological crop wilting occurs), or present abstract probabilistic statistics that cannot be understood by smallholder farmers, this study constructs a tri-task multimodal deep learning engine that simultaneously predicts: (1) physical drought hazard probabilities, (2) crop-specific prescriptive agronomic risk tiers (calibrated for tef, wheat, maize, sorghum, and haricot beans), and (3) localized acute food-security outcomes (FEWS NET / IPC Phases 1–5). Furthermore, it couples deep neural representations with Indigenous Ecological Knowledge (IEK) through a bi-directional consensus engine, ensuring cultural trust and operational adoption.")
    
    add_body(doc, "The proposed research has been structured with extreme methodological and empirical rigor to ensure completion within the standard MSc timeframe while laying a solid foundation for peer-reviewed publication in high-impact international journals and catalytic national policy deployment across the Ministry of Agriculture and Ethiopian Disaster Risk Management Commission (EDRMC).")
    
    add_body(doc, "I respectfully submit this document for your consideration, guidance, and formal approval.\n\nSincerely,\nBona Nasser Abdo\nGraduate Student, MSc Data Science Program\nDepartment of Information Science, Haramaya University\nEmail: bonanasser4@gmail.com")

    doc.add_page_break()

    # Executive Abstract
    add_heading_1(doc, "EXECUTIVE ABSTRACT")
    add_body(doc, "Smallholder rainfed agriculture in Eastern Ethiopia, particularly across Eastern Hararghe Zone, faces existential and accelerating threats from climate change, recurrent drought extremes, and climate-induced food insecurity. In late 2025 and 2026, severe multi-season rainfall deficits across the Horn of Africa pushed over 20 million people into emergency food assistance needs, highlighting the systemic failure of conventional early-warning systems. Existing operational frameworks suffer from four persistent, structural deficiencies: (1) coarse spatial resolution (GCMs and RCMs operating at 25–200 km, failing to resolve steep microclimatic gradients across rugged topography), (2) retrospective monitoring bias (satellite NDVI/VCI metrics detecting stress only after irreversible physiological crop damage has occurred), (3) a socio-technical usability gap (disseminating abstract probabilities that fail to translate into plot-level sowing dates or crop choices while completely ignoring traditional knowledge), and (4) an analytical decoupling between physical drought hazards and downstream humanitarian food-security outcomes. To overcome these profound barriers, this MSc thesis develops and empirically validates an explainable, multimodal deep learning-based early warning and prescriptive decision-support framework that bridges global climate intelligence to localized, woreda-level farm actions across Eastern Ethiopia.")
    
    add_body(doc, "The technical core of the system synthesizes a 5-tier architecture integrating physics-informed climatology, oceanic teleconnections, and multimodal deep learning. Global oceanic forcing is captured via a Conv1D-LSTM network forecasting El Niño–Southern Oscillation (Niño 3.4 SST anomalies) and Indian Ocean Dipole (IOD) trajectories up to 12 months ahead. The localized predictive engine introduces a Super-Hybrid Multimodal Deep Neural Architecture featuring five specialized branches: (a) a spatial 2D-CNN / ResNet-50 branch encoding multi-spectral satellite imagery patches (MODIS NDVI/EVI and 8-day LST), (b) a recurrent LSTM branch capturing antecedent temporal memory across hydro-climatic sequences (CHIRPS precipitation, SMAP soil moisture, ERA5 temperature/evaporation), (c) a Fast Fourier Transform (FFT) harmonic spectral branch capturing seasonal astronomical cycles and bi-annual Belg/Kiremt transitions, (d) a structured MLP/DNN branch encoding agricultural production statistics (CSA/ESS), demographic density (WorldPop), and static edaphic properties (SoilGrids), and (e) a Multimodal Gated Cross-Attention Fusion Engine that dynamically weights spatial, temporal, and tabular features into a unified latent context vector. The fused representation drives a multi-task prediction head simultaneously emitting: (i) Drought Hazard Probability P(SPI-3 <= -1), (ii) Prescriptive Crop-Specific Adjusted Risk P_adj, and (iii) Acute Food Insecurity Classification matching FEWS NET / IPC Phases (Phases 1–5).")
    
    add_body(doc, "To bridge the usability gap, drought hazard probabilities are coupled with biological crop sensitivity multipliers (s) for major regional staples (sorghum s=0.9, maize s=1.3, haricot bean s=1.1, wheat s=1.0, tef s=0.8) and mapped onto a Four-Tier Prescriptive Advisory Matrix (Low, Moderate, High, Severe Risk), generating concrete farming interventions (variety selection, tie-ridging, rainwater harvesting, planting window shifts, emergency crop pivots). Crucially, the platform incorporates a Bi-Directional Indigenous Ecological Knowledge (IEK) Consensus Engine that cross-validates AI predictions against traditional bio-climatic indicators (prevailing wind shifts, Abdim's Stork 'Shimela' migration, bee swarming, and acacia floral phenology), elevating trust among rural farming communities. Model transparency is guaranteed via Explainable AI (SHAP attributions for tabular/fused features, Grad-CAM spatial heatmaps for satellite patches, and temporal lag attribution). A Neo4j Semantic Knowledge Graph models cascading hazard-to-livelihood relationships and enables multi-hazard contextual querying. Rigorous chronological out-of-sample validation (2015–2021 training, 2022–2023 validation, 2024–2026 testing) is governed by the 'Honest Lead Horizon' principle, enforcing Brier Skill Score (BSS) gating to serve high-resolution probability maps only at validated skill leads (Lead 1) and qualitative outlooks for Leads 2–3. The entire system is packaged as an enterprise cloud-native microservice (FastAPI, PostgreSQL 17 + Star Schema for Metabase BI), a Next.js 16 Web Command Centre with role-scoped multi-tenancy (Ministers, Woreda Development Agents, Farmers), and an offline-first Expo React Native mobile field app supporting English, Amharic, and Afaan Oromoo. This research establishes an operational and scientific benchmark for AI-driven climate adaptation, food security governance, and resilient agricultural transformation across Eastern Africa.")
    
    add_callout(doc, "Keywords: Multimodal Deep Learning; Super-Hybrid CNN-LSTM-Fourier; Drought Early Warning; Prescriptive Crop Advisory; Acute Food Insecurity Prediction; FEWS NET / IPC Phases; Atmospheric Teleconnections; Self-Calibrated Palmer Drought Severity Index (Sc-PDSI); Explainable AI (SHAP & Grad-CAM); Neo4j Knowledge Graph; Indigenous Ecological Knowledge (IEK); Eastern Hararghe, Ethiopia.", title="INDEXING METADATA & KEYWORDS", alert_type="info")

    doc.add_page_break()

print("Front matter module defined.")
