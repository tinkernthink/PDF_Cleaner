import os
from PyPDF2 import PdfReader, PdfWriter
from pdfrw import PdfReader as pdfrwReader, PdfWriter as pdfrwWriter, IndirectPdfDict

# specify the directory containing your PDFs
pdf_directory = r'C:\Users\tinke\OneDrive\Desktop\New folder'

for filename in os.listdir(pdf_directory):
    if filename.endswith('.pdf'):
        pdf_path = os.path.join(pdf_directory, filename)
        
        # Remove JavaScript with PyPDF2
        pdf_reader = PdfReader(pdf_path)
        pdf_writer = PdfWriter()
        for page in pdf_reader.pages:
            pdf_writer.add_page(page)
        new_pdf_path = os.path.join(pdf_directory, f'no_js_{filename}')
        with open(new_pdf_path, 'wb') as new_pdf:
            pdf_writer.write(new_pdf)

        # Remove metadata and annotations with pdfrw
        pdf = pdfrwReader(new_pdf_path)
        pdf.Info = IndirectPdfDict()  # clear metadata
        for page in pdf.pages:
            page.Annots = None  # clear annotations
        pdfrw_writer = pdfrwWriter()
        pdfrw_writer.add_page(page)
        pdfrw_writer.write(new_pdf_path)

print('Done processing PDF files.')
