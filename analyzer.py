import docx
import fitz  # PyMuPDF

# Load keywords from file
with open("keywords.txt", "r") as f:
    keywords = [word.strip().lower() for word in f.readlines()]
    print("Keywords loaded:")
    print(keywords)
    print(type(keywords))

# DOCX extractor
def extract_text_from_docx(path):
    doc = docx.Document(path)
    return "\n".join([para.text for para in doc.paragraphs])

# PDF extractor using PyMuPDF
def extract_text_from_pdf(path):
    doc = fitz.open(path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Resume analyzer
def analyze_resume(text):
    text_lower = text.lower()
    
    score = sum(1 for kw in keywords if kw in text_lower)

    print(f"\n✅ Matched {score} out of {len(keywords)} keywords:\n")
    for kw in keywords:
        if kw in text_lower:
            print(f"✅ {kw}")
        else:
            print(f"❌ {kw}")

# File path to your resume
file_path = "resumes\sample_resume.pdf"  # You can change this to .docx too

# Extract text based on file type
if file_path.endswith(".docx"):
    content = extract_text_from_docx(file_path)
else:
    content = extract_text_from_pdf(file_path)

print(type(content))    # Debug: show type of content extracted
# Debug: show length and preview of extracted content
print(f"\n📄 Extracted text length: {len(content)}")
print(f"\n📄 Resume preview (first 300 chars):\n{content[:300]}")

# Run analysis
analyze_resume(content)
