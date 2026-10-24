"""
compile_complete_thesis_concept_note.py
Main compiler script that executes all modular builders and generates
the complete, beautifully formatted Word document.
"""

import os
import sys
import time

from build_master_concept_note import create_document
from build_front_matter import build_front_matter
from build_chapter_1 import build_chapter_1
from build_chapter_2 import build_chapter_2
from build_chapter_3 import build_chapter_3
from build_chapter_4_5_appendices import build_chapter_4_5_appendices

def compile_thesis_concept_note():
    output_filename = "AI_Multimodal_Drought_Crop_FoodInsecurity_Thesis_Concept_Note.docx"
    print(f"Starting compilation of master thesis concept note: {output_filename}...")
    start_time = time.time()
    
    doc = create_document()
    
    print("1/5 Compiling Front Matter, Cover Letter & Executive Abstract...")
    build_front_matter(doc)
    
    print("2/5 Compiling Chapter 1: Introduction, Problem Statement, Gaps & Objectives...")
    build_chapter_1(doc)
    
    print("3/5 Compiling Chapter 2: Theoretical Foundations, Climatology & Deep Learning...")
    build_chapter_2(doc)
    
    print("4/5 Compiling Chapter 3: Research Methodology, Super-Hybrid Architecture & Systems...")
    build_chapter_3(doc)
    
    print("5/5 Compiling Chapter 4, References & Appendices A-E...")
    build_chapter_4_5_appendices(doc)
    
    target_path = os.path.join(os.getcwd(), output_filename)
    doc.save(target_path)
    elapsed = time.time() - start_time
    print(f"SUCCESS: Master thesis concept note successfully compiled in {elapsed:.2f} seconds!")
    print(f"Saved at: {target_path}")
    print(f"File size: {os.path.getsize(target_path) / 1024:.2f} KB")

if __name__ == "__main__":
    compile_thesis_concept_note()
