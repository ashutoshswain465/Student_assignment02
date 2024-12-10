import glob
from fpdf import FPDF
from pathlib import Path

# Collects all text file paths in the Text_files directory
filepaths = glob.glob("Text_files/*.txt")

# Initialize a PDF object with A4 format, portrait orientation, and no automatic page breaks
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

# Loop through each file path
for filepath in filepaths:
    # Add a new page to the PDF for each text file
    pdf.add_page()
    # Extract the name of the file without the extension and capitalize it
    page_name = Path(filepath).stem.title()
    # Set the font and add the title of the page to the PDF
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=18, txt=f"{page_name}", ln=2)

    # Open the text file and read its content
    with open(filepath, 'r') as file:
        content = file.read()

    # Set the font for the content and insert the content as multi-line text
    pdf.set_font(family="Times", size=12)
    pdf.multi_cell(w=0, h=6, txt=content)

# Output the completed PDF to a file
pdf.output("output.pdf")
