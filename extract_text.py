import fitz
import os

pdf = fitz.open("data/math_book.pdf")

os.makedirs("output/text", exist_ok=True)

for page_no in range(len(pdf)):
    page = pdf.load_page(page_no)

    text = page.get_text()

    with open(f"output/text/page_{page_no+1}.txt", "w", encoding="utf-8") as f:
        f.write(text)

print("Text extraction completed.")