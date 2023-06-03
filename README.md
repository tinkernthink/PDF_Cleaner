# PDF Cleaner

This Python script processes PDF files to remove JavaScript, metadata, and annotations. It's particularly useful for preparing PDFs for upload to systems that don't support these features.

## Features

1. Removes JavaScript from PDFs.
2. Clears PDF metadata.
3. Removes annotations from PDFs.

## Usage

To use the PDF Cleaner, make sure you have Python installed on your system along with the required libraries. You can install the necessary libraries with the following command in your terminal:

```pip install PyPDF2 pdfrw```

Then, you can run the script with the following command in your terminal:

```python PDF_Cleaner.py```

## Note

Remember to back up your original files before running this script even though the changes are saved as a new file.

This script doesn't support PDFs with encryption or certain types of compression. For PDFs that cannot be processed due to these issues, consider using a more powerful library such as PDFBox or iText, but these would require Java.

