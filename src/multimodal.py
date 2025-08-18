import pdfplumber
import pandas as pd

def extract_text_from_pdf(pdf_path):
    """
    Extracts all text from a PDF file.
    Returns a single string containing all extracted text.
    """
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def extract_table_from_csv(csv_path):
    """
    Loads a CSV as a pandas DataFrame.
    Returns the DataFrame.
    """
    df = pd.read_csv(csv_path)
    return df
