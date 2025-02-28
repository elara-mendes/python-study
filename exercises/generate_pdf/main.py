import glob
from fpdf import FPDF
from pathlib import Path

texts = glob.glob("texts/*.txt")

pdf = FPDF(orientation="P", unit="mm", format="A4")

for text in texts:
    filename = Path(text).stem.capitalize()
    pdf.add_page()
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(h=0, w=50, txt=filename)
    pdf.ln(20)

    with open(text, "r") as read_mode:
        paragraph = read_mode.read()

    pdf.set_font(family="Times", size=12)
    pdf.multi_cell(h=10, w=150, txt=paragraph)

pdf.output("test.pdf")
