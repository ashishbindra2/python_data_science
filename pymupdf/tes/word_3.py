# from pdf2docx import Converter
from pdf2docx import parse

pdf_file = 'inout.pdf'
docx_file = 'sample.docx'

# convert pdf to docx
parse(pdf_file, docx_file)
