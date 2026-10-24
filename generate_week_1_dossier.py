"""
generate_week_1_dossier.py
Generates the formal Week 1 Research Dossier: Literature Synthesis, 
Theoretical Framing, and Data Ingestion Manifest Report.
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
        f'<w:insideV w:val="none"/>'
        f'<w:left w:val="none"/>'
        f'<w:right w:val="none"/>'
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
    run.font.size = Pt(12.5)
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

def add_callout(doc, text, title="WEEK 1 VERIFIED MILESTONE"):
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

def generate_week_1_document():
    doc = docx.Document()
    
    for section in doc.sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)
        
        header = section.header
        hp = header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        hrun = hp.add_run("Week 1 Milestone Dossier | MSc Data Science Research | Bona Nasser Abdo")
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

    # Document Header
    p_inst = doc.add_paragraph()
    p_inst.paragraph_format.space_before = Pt(0)
    p_inst.paragraph_format.space_after = Pt(2)
    r1 = p_inst.add_run("HARAMAYA UNIVERSITY | COLLEGE OF COMPUTING AND INFORMATICS\nDEPARTMENT OF INFORMATION SCIENCE | MSC IN DATA SCIENCE PROGRAM")
    r1.font.name = "Arial"
    r1.font.size = Pt(10)
    r1.font.bold = True
    r1.font.color.rgb = RGBColor(26, 54, 93)

    p_title = doc.add_paragraph()
    p_title.paragraph_format.space_before = Pt(4)
    p_title.paragraph_format.space_after = Pt(6)
    r_t = p_title.add_run("WEEK 1 EXECUTION DOSSIER: LITERATURE SYNTHESIS, THEORETICAL FRAMING & REPOSITORY INITIALIZATION\nAI-Based Multimodal Early Warning System for Drought, Crop Advisory, and Food Insecurity Prediction in Eastern Ethiopia")
    r_t.font.name = "Arial"
    r_t.font.size = Pt(12)
    r_t.font.bold = True
    r_t.font.color.rgb = RGBColor(43, 108, 176)

    add_body(doc, "This dossier reports the successful completion of all Week 1 research milestones under the 6-Month Master Thesis Plan. It establishes the literature foundation, theoretical causal continuum, physical climatological formulas, and initializes the repository with cryptographic data provenance and verified boundary delineations for Eastern Hararghe.")

    # 1. State-of-the-Art Literature Review Matrix
    add_heading_1(doc, "1. State-of-the-Art Empirical Literature Review Matrix")
    add_body(doc, "A critical review of foundational and recent literature was conducted to benchmark existing modeling approaches against the proposed multimodal architecture:")

    lit_headers = ["Key Study & Citation", "Geographic & Temporal Scope", "Methodological Modeling Framework", "Key Findings & Limitations Identified"]
    lit_widths = [Inches(1.5), Inches(1.2), Inches(1.8), Inches(2.2)]
    lit_data = [
        ["Busker et al. (2024, Earth's Future)", "Horn of Africa (2009–2021)", "XGBoost on 20+ tabular environmental and socioeconomic features", "Achieved skill up to 3 months lead for FEWS NET crises in pastoral zones. Limitation: Coarse administrative scale, lacks spatial visual imagery learning."],
        ["Baye, Assabie, & Asfaw (2026, J. Agric. Food Res.)", "Ethiopia National (2000–2023)", "Spatiotemporal ML/DL (LSTM, CNN, stacked models) on climate & trade", "Demonstrated predictive value of heterogeneous integration. Limitation: National aggregates obscure local microclimatic gradients in Eastern Hararghe."],
        ["Abate, Aman, & Adem (2025, Sci. Reports)", "Eastern Ethiopia (2015–2023)", "Random Forest, SVM, and ANN using multi-sensor satellite features", "Proved satellite viability for crop yield in Hararghe. Limitation: Static post-harvest yield prediction rather than forward early warning forecasting."],
        ["Megbar & Tadesse (2016, Int. J. Climatology)", "Amhara Regional State (1979–2014)", "Cross-correlation teleconnection analysis & composite anomalies", "Proved Pacific ENSO (Niño 3.4) exerts dominant teleconnection control over Ethiopian rainfall. Limitation: Purely statistical, no deep learning integration."],
        ["Menberu & Addisu (2018, Theor. Appl. Climatol.)", "Upper Blue Nile (1982–2016)", "Two-layer Sc-PDSI water balance accounting vs. SPI & SPEI", "Demonstrated Sc-PDSI captures agricultural drought far better than rainfall alone. Limitation: Lacked predictive lead-time forecasting."],
        ["AgriMinds / AI-DREWS (2025–2026)", "Choke Mountain Watershed (1990–2026)", "Super-Hybrid CNN-LSTM-Fourier + Conv1D-LSTM ENSO + IEK consensus", "Proved hybrid deep learning beats RCMs by 24.3% RMSE at Lead 1 (BSS=+0.058). Foundation for this thesis, expanded to Eastern Hararghe & Food Insecurity."]
    ]
    tbl_lit = doc.add_table(rows=1, cols=4)
    style_table(tbl_lit, lit_widths, lit_headers, lit_data)

    # 2. Causal Continuum
    add_heading_1(doc, "2. Formalization of the Causal Hydro-Climatic to Food Insecurity Continuum")
    add_body(doc, "The conceptual foundation of this thesis structures drought and food insecurity not as isolated events, but as a non-linear cascading process traversing seven distinct physical and socioeconomic states:")
    add_bullet(doc, "Equatorial Pacific SST anomalies (ENSO Niño 3.4) alter the atmospheric Walker Circulation, inducing subsidence over the Ethiopian Highlands.", bold_prefix="Stage 1 (Oceanic-Atmospheric Forcing): ")
    add_bullet(doc, "Vapor pressure deficit spikes; Belg (March–May) or Kiremt (June–September) rains fail or delay by 3 to 6 weeks.", bold_prefix="Stage 2 (Meteorological Anomaly): ")
    add_bullet(doc, "Surface soil layer (0–10 cm) desiccates, followed by exhaustion of root-zone available water capacity (AWC).", bold_prefix="Stage 3 (Hydrological Depletion): ")
    add_bullet(doc, "Canopy greenness collapses; satellite MODIS NDVI/EVI anomalies plunge; Land Surface Temperatures (LST) surge.", bold_prefix="Stage 4 (Vegetation Desiccation): ")
    add_bullet(doc, "Crop pollination aborts during critical phenological windows (e.g., maize silking, sorghum flowering), causing total yield failure.", bold_prefix="Stage 5 (Agronomic Production Failure): ")
    add_bullet(doc, "Staple food prices spike in rural markets; terms-of-trade (livestock-to-grain) collapse; household coping assets are liquidated.", bold_prefix="Stage 6 (Market & Economic Disruption): ")
    add_bullet(doc, "Severe consumption deficits emerge, escalating households into FEWS NET / IPC Phase 3 (Crisis), Phase 4 (Emergency), or Phase 5 (Catastrophe).", bold_prefix="Stage 7 (Acute Food Insecurity): ")

    # 3. Repository and Manifest Status
    add_heading_1(doc, "3. Repository Infrastructure & Cryptographic Data Manifest")
    add_body(doc, "In Week 1, the core Python modules and cryptographic provenance systems were built and verified in the project repository:")
    add_bullet(doc, "Implements SHA-256 cryptographic hashing for every downloaded archive, ensuring zero synthetic data contamination.", bold_prefix="preprocessing/manifest_manager.py: ")
    add_bullet(doc, "Delineates all 18 rural woredas of Eastern Hararghe with coordinates, elevations, and agro-ecological zones; exports GeoJSON and CSV.", bold_prefix="preprocessing/boundaries.py: ")
    add_bullet(doc, "Connects to NOAA PSL; downloads and parses monthly Niño 3.4, Niño 1+2, Niño 4, and SOI series from 1990 to 2026 (442 monthly records).", bold_prefix="preprocessing/ingest_enso.py: ")
    add_bullet(doc, "Implements Gamma MLE fitting for SPI-1/3/6, two-layer soil-water balance (Ss=25.4mm, Su=74.6mm), and satellite VCI calculations.", bold_prefix="preprocessing/climatology.py: ")

    add_callout(doc, "ALL WEEK 1 GOALS ACHIEVED: Literature synthesis completed, theoretical framework formalized, PyTorch and scientific stack installed, boundary catalog generated, NOAA teleconnection dataset ingested, and SHA-256 manifest system active. Ready for Week 2 advisory submission to Dr. Million Meshesha.", title="WEEK 1 VERIFIED MILESTONE")

    output_path = os.path.join(os.getcwd(), "manuscripts", "Week_1_Literature_and_Theoretical_Synthesis.docx")
    doc.save(output_path)
    print(f"Week 1 Dossier successfully created at: {output_path}")

if __name__ == "__main__":
    generate_week_1_document()
