import fitz
class PDFParser:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path

    def extract_text(self):
        with fitz.open(self.pdf_path) as doc:
            text = ""
            for page_num in range(3, len(doc)):  # Start reading from the 4th page (index 3 ,as earlier are introduction)
                page = doc.load_page(page_num)  # Load each page after the first 3
                text += page.get_text() 
        return text
    def chunk_pdf(self, chunk_size=300):
        text = self.extract_text()
        words = text.split()
        return [' '.join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]
