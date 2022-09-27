from PyPDF2 import PdfFileWriter, PdfFileReader
import getpass

pdf_writer = PdfFileWriter()
pdf_file = PdfFileReader("file.pdf")

for page_num in range(pdf_file.numPages):
    pdf_writer.addPage(pdf_file.getPage(page_num))

password = getpass.getpass(prompt='Enter Password: ')
pdf_writer.encrypt(password)

with open('result.pdf', 'wb') as f:
    pdf_writer.write(f)
