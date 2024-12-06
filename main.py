import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("Text_files/*.txt")

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

for filepath in filepaths:
    pdf.add_page()
    page_name = Path(filepath).stem.title()
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=18, txt=f"{page_name}")

pdf.output("output.pdf")
