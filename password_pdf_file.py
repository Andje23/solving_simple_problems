import getpass

from PyPDF2 import PdfFileWriter, PdfFileReader

password: str = getpass.getpass(prompt='Enter Password: ')


def adding_password_to_pdf_file(*, file_name_and_path: str = "file.pdf", name_result_file: str = 'result.pdf',
                                password: str = password) -> None:
    pdf_writer = PdfFileWriter()
    pdf_file = PdfFileReader(file_name_and_path)

    for page_num in range(pdf_file.numPages):
        pdf_writer.addPage(pdf_file.getPage(page_num))

    pdf_writer.encrypt(password)

    with open(name_result_file, 'wb') as file:
        pdf_writer.write(file)
