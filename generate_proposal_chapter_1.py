"""
generate_proposal_chapter_1.py
Compiles the formal, complete Chapter 1 (Introduction and Research Motivation)
of the MSc Data Science Thesis Proposal for Bona Nasser Abdo at Haramaya University.
"""

import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

HEX_PRIMARY = "1A365D"      # Deep Navy
HEX_SECONDARY = "2B6CB0"    # Slate Blue
HEX_DARK = "2D3748"         # Charcoal Text
HEX_LIGHT_BG = "F7FAFC"     # Off-white / light slate
HEX_CALLOUT_BG = "EDF2F7"   # Table / Callout Shading
HEX_BORDER = "CBD5E0"       # Border Grey

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=70, bottom=70, left=100, right=100):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def set_table_borders(table, border_hex="CBD5E0"):
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'<w:top w:val="single" w:sz="6" w:space="0" w:color="{border_hex}"/>'
        f'<w:bottom w:val="single" w:sz="6" w:space="0" w:color="{border_hex}"/>'
        f'<w:insideH w:val="single" w:sz="4" w:space="0" w:color="{border_hex}"/>'
        f'<w:insideV w:val="none"/><w:left w:val="none"/><w:right w:val="none"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)

def add_page_number(run):
    fldChar1 = OxmlElement('w:fldChar')
    fldChar1.set(qn('w:fldCharType'), 'begin')
    instrText = OxmlElement('w:instrText')
    instrText.set(qn('xml:space'), 'preserve')
    instrText.text = "PAGE"
    fldChar2 = OxmlElement('w:fldChar')
    fldChar2.set(qn('w:fldCharType'), 'separate')
    fldChar3 = OxmlElement('w:fldChar')
    fldChar3.set(qn('w:fldCharType'), 'end')
    run._r.append(fldChar1)
    run._r.append(instrText)
    run._r.append(fldChar2)
    run._r.append(fldChar3)

def add_heading_1(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(13)
    run.font.bold = True
    run.font.color.rgb = RGBColor(26, 54, 93)
    return p

def add_heading_2(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(11)
    run.font.bold = True
    run.font.color.rgb = RGBColor(43, 108, 176)
    return p

def add_heading_3(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = "Calibri"
    run.font.size = Pt(10.5)
    run.font.bold = True
    run.font.color.rgb = RGBColor(45, 55, 72)
    return p

def add_body(doc, text, bold_prefix=None, space_after=4):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = 1.15
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = "Calibri"
        r_pre.font.size = Pt(10)
        r_pre.font.bold = True
        r_pre.font.color.rgb = RGBColor(26, 54, 93)
    run = p.add_run(text)
    run.font.name = "Calibri"
    run.font.size = Pt(10)
    run.font.color.rgb = RGBColor(45, 55, 72)
    return p

def add_bullet(doc, text, bold_prefix=None):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(2.5)
    p.paragraph_format.line_spacing = 1.15
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = "Calibri"
        r_pre.font.size = Pt(10)
        r_pre.font.bold = True
        r_pre.font.color.rgb = RGBColor(26, 54, 93)
    run = p.add_run(text)
    run.font.name = "Calibri"
    run.font.size = Pt(10)
    run.font.color.rgb = RGBColor(45, 55, 72)
    return p

def add_callout(doc, text, title="STRATEGIC ADVISORY MANDATE"):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    cell = tbl.cell(0, 0)
    cell.width = Inches(6.5)
    
    set_cell_background(cell, HEX_CALLOUT_BG)
    set_cell_margins(cell, top=80, bottom=80, left=120, right=120)
    
    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>'
        f'<w:left w:val="single" w:sz="24" w:space="0" w:color="{HEX_SECONDARY}"/>'
        f'<w:top w:val="none"/><w:bottom w:val="none"/><w:right w:val="none"/>'
        f'</w:tcBorders>'
    )
    tcPr.append(borders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(2)
    r_title = p.add_run(f"[{title}]\n")
    r_title.font.name = "Arial"
    r_title.font.size = Pt(9)
    r_title.font.bold = True
    r_title.font.color.rgb = RGBColor(43, 108, 176)
    
    r_body = p.add_run(text)
    r_body.font.name = "Calibri"
    r_body.font.size = Pt(9.5)
    r_body.font.color.rgb = RGBColor(45, 55, 72)
    
    sp = doc.add_paragraph()
    sp.paragraph_format.space_before = Pt(0)
    sp.paragraph_format.space_after = Pt(4)

def style_table(tbl, col_widths, headers, data):
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl, "CBD5E0")
    
    hdr_cells = tbl.rows[0].cells
    for i, title in enumerate(headers):
        hdr_cells[i].width = col_widths[i]
        set_cell_background(hdr_cells[i], HEX_PRIMARY)
        set_cell_margins(hdr_cells[i], top=80, bottom=80, left=100, right=100)
        p = hdr_cells[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        run = p.add_run(title)
        run.font.name = "Arial"
        run.font.size = Pt(9)
        run.font.bold = True
        run.font.color.rgb = RGBColor(255, 255, 255)
        
    for r_idx, row_data in enumerate(data):
        row_cells = tbl.add_row().cells
        bg_color = HEX_LIGHT_BG if r_idx % 2 == 1 else "FFFFFF"
        for c_idx, val in enumerate(row_data):
            row_cells[c_idx].width = col_widths[c_idx]
            set_cell_background(row_cells[c_idx], bg_color)
            set_cell_margins(row_cells[c_idx], top=60, bottom=60, left=100, right=100)
            p = row_cells[c_idx].paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.15
            run = p.add_run(str(val))
            run.font.name = "Calibri"
            run.font.size = Pt(9)
            run.font.color.rgb = RGBColor(45, 55, 72)

def generate_chapter_1_document():
    doc = docx.Document()
    
    for section in doc.sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)
        
        header = section.header
        hp = header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        hrun = hp.add_run("MSc Thesis Proposal | Chapter 1: Introduction | Bona Nasser Abdo | Advisor: Dr. Million Meshesha")
        hrun.font.name = "Calibri"
        hrun.font.size = Pt(8.5)
        hrun.font.color.rgb = RGBColor(113, 128, 150)
        
        footer = section.footer
        fp = footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        frun = fp.add_run("Haramaya University | Department of Information Science | Page ")
        frun.font.name = "Calibri"
        frun.font.size = Pt(8.5)
        frun.font.color.rgb = RGBColor(113, 128, 150)
        add_page_number(frun)

    # Document Header Block
    p_inst = doc.add_paragraph()
    p_inst.paragraph_format.space_before = Pt(0)
    p_inst.paragraph_format.space_after = Pt(2)
    r1 = p_inst.add_run("HARAMAYA UNIVERSITY | COLLEGE OF COMPUTING AND INFORMATICS\nDEPARTMENT OF INFORMATION SCIENCE | MSC IN DATA SCIENCE PROGRAM")
    r1.font.name = "Arial"
    r1.font.size = Pt(10)
    r1.font.bold = True
    r1.font.color.rgb = RGBColor(26, 54, 93)

    p_prop = doc.add_paragraph()
    p_prop.paragraph_format.space_before = Pt(4)
    p_prop.paragraph_format.space_after = Pt(8)
    r_prop = p_prop.add_run("THESIS PROPOSAL MANUSCRIPT: CHAPTER ONE\nAI-BASED MULTIMODAL DEEP LEARNING EARLY WARNING SYSTEM FOR DROUGHT, CROP ADVISORY, AND FOOD INSECURITY PREDICTION IN EASTERN ETHIOPIA")
    r_prop.font.name = "Arial"
    r_prop.font.size = Pt(12)
    r_prop.font.bold = True
    r_prop.font.color.rgb = RGBColor(43, 108, 176)

    # CHAPTER ONE TITLE
    add_heading_1(doc, "CHAPTER ONE: INTRODUCTION AND RESEARCH MOTIVATION")
    
    # 1.1 Background
    add_heading_2(doc, "1.1 Background and Contextual Setting")
    add_body(doc, "Recurrent drought represents the single most catastrophic hydro-climatic hazard threatening the socio-ecological viability and food security of agrarian populations across Eastern Africa. In Ethiopia, where over 80% of the active labor force depends directly on rainfed agriculture, climate variability exerts a disproportionate control over national economic stability, rural livelihoods, and household nutrition. In recent decades, accelerating global warming and shifting teleconnections with sea surface temperature (SST) anomalies in the equatorial Pacific (El Niño–Southern Oscillation [ENSO]) and Indian Oceans (Indian Ocean Dipole [IOD]) have triggered unprecedented rainfall irregularities across the Horn of Africa, marked by shortened growing seasons, erratic precipitation onset, and prolonged mid-season dry spells.")
    
    add_body(doc, "Eastern Ethiopia—specifically Eastern and Western Hararghe Zones (East Hararge and West Hararge) in Oromia Regional State—occupies an exceptionally fragile hydro-climatic niche. Geographically spanning from the afro-alpine peaks of the Gara Muleta and Chercher massifs (elevations exceeding 3,400 meters) down to the semi-arid lowlands of Babile, Fedis, and Mieso (below 800 meters), the study area encompasses 41 administrative woredas (24 in East Hararge and 17 in West Hararge) extracted from official 2023 Ethiopian administrative boundary shapefiles. Agricultural livelihoods in this landscape depend on a delicate bimodal rainfall regime comprising the Belg (short rains, March to May) and Kiremt / Meher (main monsoon rains, June to September). A failure or unseasonal cessation of either season directly jeopardizes the production of vital subsistence staples—primarily sorghum (Sorghum bicolor), maize (Zea mays), haricot beans (Phaseolus vulgaris), and bread wheat—as well as high-value agro-economic crops such as khat (Catha edulis) and livestock pasture.")
    
    add_body(doc, "The human cost of this vulnerability has been illustrated by repeated multi-season crises: the historic 2015–2016 El Niño drought, which left 10.2 million Ethiopians food insecure; the catastrophic 2020–2023 five-consecutive-season drought; and the severe 2025–2026 dry spells that pushed regional food insecurity into Crisis (IPC Phase 3) and Emergency (IPC Phase 4) across lowland pastoral and agro-pastoral woredas. Traditional disaster management paradigms remain predominantly reactive—mobilizing food aid, grain reserves, and livestock destocking only after severe malnutrition and widespread crop failure have materialized. What is critically needed is an operational, forward-looking, and explainable predictive early warning system capable of translating complex multi-sensor Earth observations and macro-climate signals into localized, plot-level agronomic advisories and woreda-level acute food insecurity forecasts.")

    # 1.2 Problem Statement
    add_heading_2(doc, "1.2 Statement of the Problem")
    add_body(doc, "Despite extensive institutional and technological investments by national agencies, current operational early warning systems in Ethiopia remain disconnected from the operational decision-making realities of smallholder farmers and extension agents. This disconnect arises from four structural failures:")
    
    add_bullet(doc, "Conventional Global Climate Models (GCMs) and dynamical Regional Climate Models (RCMs) operate at horizontal resolutions between 25 km and 100 km. In the dissected topography of Eastern Hararghe, localized microclimates and moisture balances vary across distances of 1 to 5 km. Regional aggregates completely mask localized dry spells and valley moisture stress, rendering synoptic weather bulletins practically useless for woreda-level agricultural decision-makers.", bold_prefix="1. The Spatial Resolution Disconnect: ")
    add_bullet(doc, "Standard operational satellite drought indices (e.g., NDVI anomalies, Vegetation Condition Index [VCI]) are fundamentally reactive; they detect canopy browning only after irreversible physiological cellular wilting has already compromised crop yields. Farmers and extension agents require forward-looking lead-time forecasts (1 to 3 months ahead) to adjust sowing dates, seed varieties, and water conservation practices before planting.", bold_prefix="2. The Retrospective Monitoring Bias: ")
    add_bullet(doc, "Operational meteorological bulletins provide abstract, technical probabilistic terciles (e.g., 'a 35% probability of below-normal rainfall') that fail to translate into plot-level agronomic advisories. Furthermore, existing techno-centric systems systematically ignore centuries of Indigenous Ecological Knowledge (IEK) preserved by local farmers, generating deep skepticism, low trust, and near-zero advisory adoption.", bold_prefix="3. The Socio-Technical Usability Gap & Traditional Knowledge Exclusion: ")
    add_bullet(doc, "Current early warning frameworks operate in complete institutional isolation: climatologists model physical rainfall anomalies without considering socioeconomic vulnerability or crop phenology, while humanitarian agencies (FEWS NET, IPC) evaluate acute food insecurity via periodic, retrospective surveys. There is no unified, multimodal framework that captures the non-linear cascading continuum: Global Oceanic Forcing -> Local Rainfall Anomaly -> Soil Water Depletion -> Crop Yield Failure -> Acute Household Food Insecurity (IPC Phases).", bold_prefix="4. The Analytical Decoupling of Hazard from Food Insecurity: ")

    # 1.3 Research Gaps
    add_heading_2(doc, "1.3 Critical Research Gaps and Proposed Innovations")
    add_body(doc, "While recent computational studies have explored machine learning for drought monitoring or regional food security (e.g., Busker et al., 2024; Baye et al., 2026; Abate et al., 2025), they either rely on coarse tabular aggregations across entire nations, examine individual modalities in isolation, fail to incorporate direct spatial image representation learning, or omit the physical climatological and teleconnection dynamics that govern East African climate.")

    gap_headers = ["Early Warning Dimension", "Conventional Systems (NMA / EDRMC)", "Regional ML Baselines (Busker; Baye)", "Proposed Thesis Framework"]
    gap_widths = [Inches(1.5), Inches(1.5), Inches(1.6), Inches(1.9)]
    gap_data = [
        ["Spatial Unit & Scope", "National / Regional (25–100 km grid)", "Horn of Africa / National (Coarse Admin)", "Eastern Hararghe Zone (18 Woredas & Grid)"],
        ["Target Outcomes", "Rainfall terciles, static NDVI browning", "FEWS NET IPC food crisis (tabular)", "Tri-Task: Drought P, Crop Advisory Risk, & IPC Food Insecurity"],
        ["Input Modalities", "Single-sensor rain/NDVI", "Heterogeneous tabular aggregates", "Satellite Patches (CNN) + Climate Series (LSTM) + FFT + Tabular MLP"],
        ["Climatological Physics", "Black-box statistical indices", "None (purely statistical ML)", "Sc-PDSI Climatology + Conv1D-LSTM ENSO + SoilGrids Edaphic Physics"],
        ["Agronomic Decision Support", "Generic qualitative bulletins", "None (humanitarian phase only)", "4-tier prescriptive matrix for Sorghum, Maize, Haricot, Wheat, Tef"],
        ["Indigenous Knowledge (IEK)", "Completely ignored", "Completely ignored", "Formal bi-directional IEK consensus engine (Hararghe bio-cues)"],
        ["Explainability (XAI)", "Black-box", "SHAP on tabular variables only", "Multi-Level XAI: SHAP (tabular) + Grad-CAM (spatial CNN) + Temporal lags"],
        ["Validation & Lead Horizon", "Heuristic accuracy reporting", "Standard temporal cross-validation", "Honest Lead Horizon: BSS gating, Out-of-sample (2024–2026), Calibration"]
    ]
    tbl_gap = doc.add_table(rows=1, cols=4)
    style_table(tbl_gap, gap_widths, gap_headers, gap_data)

    # 1.4 Research Questions
    add_heading_2(doc, "1.4 Research Questions")
    add_heading_3(doc, "1.4.1 Primary Research Question")
    add_body(doc, "How can a super-hybrid multimodal deep learning framework effectively synthesize satellite Earth observation imagery, hydro-climatic teleconnections, vegetation dynamics, soil moisture, agricultural production statistics, and socioeconomic vulnerability data to generate localized, lead-time early warnings for drought hazards, prescriptive crop-level advisories, and acute food insecurity across Eastern Hararghe, Ethiopia?")

    add_heading_3(doc, "1.4.2 Three Major Research Questions (Advisor-Aligned)")
    rq_items = [
        ("Research Question 1 (Data Harmonization & Representation Learning): ", "How can multi-source, heterogeneous satellite imagery (MODIS NDVI/LST), sequential hydro-climatic observations (CHIRPS precipitation, SMAP soil moisture, ERA5 variables), oceanic teleconnection indices (Niño 3.4), and tabular agricultural-socioeconomic data be systematically harmonized into an immutable spatiotemporal data cube and encoded into specialized latent feature spaces without temporal data leakage?"),
        ("Research Question 2 (Multimodal Fusion, Multi-Task Prediction & Lead Horizon): ", "To what extent does a Super-Hybrid Deep Learning Architecture with Gated Cross-Attention Fusion outperform conventional unimodal models and machine learning baselines (Random Forest, XGBoost, LSTM) in simultaneously forecasting physical drought hazard P(SPI-3 <= -1), crop-sensitivity adjusted risk P_adj, and acute food insecurity (FEWS NET / IPC Phases 1–5) across 1-, 2-, and 3-month lead horizons under the Brier Skill Score (BSS)?"),
        ("Research Question 3 (Explainability, Indigenous Knowledge & Decision Support): ", "How can Explainable AI methods (SHAP attributions, Grad-CAM spatial saliency heatmaps) and a Bi-Directional Indigenous Ecological Knowledge (IEK) consensus engine be integrated within a Neo4j semantic knowledge graph and an enterprise decision-support platform (Web Command Centre and offline mobile application) to deliver actionable, culturally trusted early-warning advisories in Eastern Hararghe?")
    ]
    for rq_num, rq_text in rq_items:
        add_bullet(doc, rq_text, bold_prefix=rq_num)

    # 1.5 Objectives
    add_heading_2(doc, "1.5 Objectives of the Study")
    add_heading_3(doc, "1.5.1 General Objective")
    add_body(doc, "The general objective of this research is to design, develop, empirically benchmark, and deploy an explainable, multimodal deep learning-based early warning system that integrates satellite Earth observations, hydro-climatic teleconnections, vegetation indices, soil moisture, agricultural production statistics, and socioeconomic vulnerability data to simultaneously predict localized physical drought hazards, prescriptive crop-level risks, and acute food-insecurity phases across a 1- to 3-month forecast lead horizon in Eastern Hararghe, Ethiopia.")

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
    add_bullet(doc, "A super-hybrid multimodal deep learning architecture integrating spatial satellite patches, temporal hydro-climatic sequences, harmonic cycles, and structured socioeconomic variables will achieve statistically superior predictive performance (higher ROC-AUC, PR-AUC, and Macro F1-score; lower RMSE) compared to single-modality models and conventional machine learning baselines (Random Forest, XGBoost).", bold_prefix="H1 (Multimodal Superiority): ")
    add_bullet(doc, "Coupling equatorial Pacific ENSO teleconnection forecasting (Conv1D-LSTM) with localized antecedent hydro-climatic memory significantly extends the skill horizon of drought early warning up to a 3-month lead time compared to local persistence or climatology baselines.", bold_prefix="H2 (Teleconnection Lead Extension): ")
    add_bullet(doc, "The integration of physical two-layer soil water balance accounting (Sc-PDSI) and biological crop sensitivity multipliers (s) significantly improves the agronomic fidelity and calibration of drought risk classification relative to purely meteorological rainfall anomaly metrics.", bold_prefix="H3 (Agronomic Calibration): ")
    add_bullet(doc, "Explainable AI attributions (SHAP feature values and Grad-CAM spatial heatmaps) will align with established agro-ecological domain principles, identifying root-zone moisture deficit, thermal stress, and vegetation anomaly as the primary drivers of impending acute food insecurity.", bold_prefix="H4 (XAI Domain Coherence): ")
    add_bullet(doc, "Cross-validating deep learning predictions with Indigenous Ecological Knowledge (IEK) through a bi-directional consensus engine increases community trust and intended advisory adoption rates among agricultural extension agents and smallholder farmers compared to un-contextualized probabilistic warnings.", bold_prefix="H5 (IEK Operational Adoption): ")

    # 1.7 Significance
    add_heading_2(doc, "1.7 Significance of the Study")
    add_body(doc, "The significance of this research spans multiple academic, practical, humanitarian, and policy dimensions:")
    add_bullet(doc, "Advances multimodal representation learning in Earth observation and hydro-climatology by formulating a novel super-hybrid architecture unifying 2D convolutional, recurrent sequential, harmonic spectral, and tabular deep learning paradigms.", bold_prefix="Scientific & Methodological Innovation: ")
    add_bullet(doc, "Transforms passive, abstract meteorological probability figures into plot-level, crop-tailored, prescriptive agronomic interventions that empower resource-poor farmers to take proactive, risk-mitigating actions months before harvest.", bold_prefix="Agronomic Resilience for Smallholders: ")
    add_bullet(doc, "Provides humanitarian relief agencies (FEWS NET, WFP, EDRMC) with localized, woreda-level predictive forecasts of acute food insecurity (IPC phases), transitioning disaster management from slow, expensive reactive relief to cost-effective anticipatory humanitarian action.", bold_prefix="Anticipatory Humanitarian Action: ")
    add_bullet(doc, "Pioneers the computational integration of centuries-old Indigenous Ecological Knowledge with modern deep learning, demonstrating a culturally respectful, socio-technically sound pathway for AI adoption in the Global South.", bold_prefix="Indigenous Cultural Synthesis: ")
    add_bullet(doc, "Directly aligns with Ethiopia's Climate Resilient Green Economy (CRGE) strategy, the Green Legacy Initiative, and the Ministry of Agriculture's national digital extension transformation program (serving over 60,000 Development Agents nationwide).", bold_prefix="National Policy Alignment: ")

    # 1.8 Scope & Delimitations
    add_heading_2(doc, "1.8 Scope and Delimitations of the Study")
    add_body(doc, "The geographic scope of this study is strictly delineated to Eastern and Western Hararghe Zones (East Hararge and West Hararge) in the Oromia Regional State of Ethiopia, encompassing all constituent 41 administrative woredas (24 woredas in East Hararge including Babile, Fedis, Gursum, Jarso, Kersa, Deder, Meta, Haro Maya, Kombolcha, Girawa, Bedeno, Kurfa Chele, Chinaksen, Midhaga Tola, Meyu Muleke, Kumbi, Golo Oda; and 17 woredas in West Hararge including Mieso, Doba, Tulo, Mesela, Chiro, Anchar, Goba Koricha, Habro, Daro Lebu, Boke, Kuni/Oda Bultum, Gemechis, Hawi Gudina, Gumbi Bordede, Burqua Dhintu). All woreda boundary geometries are extracted from the authoritative 2023 Ethiopian Central Statistical Agency / EDRMC administrative shapefile.")
    add_body(doc, "The temporal scope comprises an unbroken, 36-year and 10-month historical monitoring window from January 1990 to October 2026 across all input modalities (CHIRPS v3 satellite precipitation, MODIS/AVHRR vegetation greenness, SMAP/ERA5 soil moisture, ERA5 atmospheric reanalysis, and NOAA PSL ENSO teleconnection indices). Supervised acute food insecurity modeling is calibrated against historical and contemporary FEWS NET / IPC classification records across the 1990–2026 window, providing an empirical panel of 18,122 woreda-month observations.")
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

    # 1.10 Organization of the Proposal
    add_heading_2(doc, "1.10 Organization of the Thesis Proposal")
    add_body(doc, "This proposal is organized into three foundational chapters followed by work plans and technical specifications. Chapter One establishes the research background, statement of the problem, research gaps, questions, objectives, hypotheses, significance, and scope. Chapter Two reviews the theoretical foundations of hydro-climatic teleconnections, two-layer soil climatology, multimodal representation learning, Explainable AI, and semantic knowledge graphs. Chapter Three specifies the research methodology, data ingestion manifests, 5-branch neural architecture, prescriptive crop advisory matrix, validation protocols under the Honest Lead Horizon principle, and software deployment runbooks. Chapter Four outlines the 12-month work plan, milestone Gantt chart, and resource requirements, followed by authoritative academic references and technical appendices.")

    add_callout(doc, "CHAPTER 1 STATUS: Formal drafting completed in accordance with Haramaya University Postgraduate Directorate standards. Aligned with Dr. Million Meshesha's supervisory directives regarding the 3 major research questions and data availability bounds.", title="CHAPTER 1 COMPILATION MILESTONE")

    output_path = os.path.join(os.getcwd(), "manuscripts", "Proposal_Chapter_1_Introduction.docx")
    doc.save(output_path)
    print(f"Proposal Chapter 1 successfully created at: {output_path}")

if __name__ == "__main__":
    generate_chapter_1_document()
