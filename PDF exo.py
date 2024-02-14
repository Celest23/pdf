from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    # set the header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(86, 10, 23)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L",
             ln=1)                # the last 10 means it will be repeated every 10 times
    for y in range(20, 298, 10):  # this creates multiple lines, these are ranges
        pdf.line(10, y, 200, y)  # 10 is from the beginning of the line,
        # y is 20 from bottom of the line to top
        # 200 is the length of the line and 20 again for y
        # this will be repeated every 10 times




    #set the footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    for i in range(row["Pages"] - 1):
        pdf.add_page()
        #set the footer again
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

        for y in range(20, 298, 10):
            pdf.line(10, y, 200, y)

pdf.output("pdfexo.pdf")