import fitz # this help you to extract the txt from pdf 
import os 


def extract_text_from_pdf(pdf_path: str):
    doc = fitz.open(pdf_path)
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    return full_text    

def build_index_pdf(pdf_path: str, persist_dir: str = "./rag_store"):
    full_text = extract_text_from_pdf(pdf_path)
    print(full_text)

if __name__ == "__main__":
    build_index_pdf(r"C:\Users\abhis\OneDrive\Desktop\RAG_Agent_Assistant\docs\sample_rental_agreement.pdf")