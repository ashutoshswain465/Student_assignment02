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
    pdf.cell(w=50, h=18, txt=f"{page_name}", ln=2)

    with open(filepath, 'r') as file:
        content = file.read()

    pdf.set_font(family="Times", size=12)
    pdf.multi_cell(w=0, h=6, txt=content)

pdf.output("output.pdf")
