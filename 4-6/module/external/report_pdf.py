"""import reportlab
for attr in dir(reportlab):
    print attr

"""
from reportlab.pdfgen import canvas
from reportlab.lib import pdfencrypt
pdf = canvas.Canvas("spec.pdf")
#abc = "shgffgsjfgsgfsgfsj fjfs jfgjsfgsjfg fg fg sfgshfgshfgs"
pdf.drawString(10,10,"hello")
pdf = canvas.Canvas("spec.pdf",bottomup=0)
pdf.drawString(10,10,"Spectrum Technologies")
pdf.showPage()


pdf.drawString(10,10,"hello Spectrum Technologies")
pdf.showPage()
pdf.save()

