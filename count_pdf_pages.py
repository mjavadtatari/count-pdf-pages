from glob import glob
import PyPDF2

file_list = glob("*.pdf")

totalpages = 0

for i in file_list:
    file = open(i, 'rb')
    readpdf = PyPDF2.PdfFileReader(file)
    totalpages += readpdf.numPages

print(totalpages)
