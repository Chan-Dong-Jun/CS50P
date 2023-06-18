#02/06/2023
#CS50P Week 8

from fpdf import FPDF
import fpdf

text = f"{input('Name: ')} took CS50"

pdf = FPDF(format="A4")
pdf.set_font("Times", size=36)
pdf.add_page()
pdf.image("shirtificate.png", w=pdf.epw, y=pdf.epw/4)
pdf.cell(txt="CS50 Shirtificate", w=pdf.epw, align= fpdf.enums.Align.C)
pdf.set_xy(10, pdf.eph/2)
pdf.set_font("Times", size=25)
pdf.set_text_color(255, g=255, b=255)
pdf.cell(txt=text, w=pdf.epw, align=fpdf.enums.Align.C)
pdf.output("shirtificate.pdf")