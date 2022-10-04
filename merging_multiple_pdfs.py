import os

from PyPDF2 import PdfFileMerger
from loguru import logger

logger.add("password_pdf_file.log", format="{time} {level} {message}",
           level="DEBUG", rotation="1 MB", compression="zip")


@logger.catch
def merge_multiple_pdf() -> None:
    merger = PdfFileMerger()
    for items in os.listdir():
        if items.endswith('.pdf'):
            merger.append(items)
    merger.write('combined_pdf_file.pdf')
    merger.close()
