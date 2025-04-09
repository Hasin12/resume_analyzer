# 📄 Resume Analyzer

A simple Python script that analyzes resumes (`.pdf` or `.docx`) by checking for the presence of specific keywords. It's useful for quickly evaluating how well a resume aligns with a set of desired skills or job requirements.

## How It Works

1. **Input**: A resume file (`.pdf` or `.docx`) located in the `resumes/` folder.
2. **Keywords**: A list of target keywords is stored in `keywords.txt`.
3. **Output**: The script reads and processes the resume, then prints:
   - The number of matched keywords.
   - A checklist showing which keywords are present or missing.

## 🛠️ Requirements

Make sure you have Python 3 installed and then install the required packages:

```bash
pip install python-docx PyMuPDF
# Project Structure
resume-analyzer/
├── analyzer.py          # Main script
├── keywords.txt         # List of keywords (one per line)
├── resumes/
│   └── sample_resume.pdf  # Your resume file here
└── README.md
# How to Run

1. Add Resume
2. Place your .pdf or .docx resume in the resumes/ folder.
3. Add Keywords
4. Populate keywords.txt with one keyword per line.
5. Update File Path
6. In analyzer.py, set the resume file path:

#Sample Output
✅ Matched 5 out of 8 keywords:

✅ python
✅ sql
❌ javascript
✅ pandas
...
#Notes
1. Ensure your file paths use forward slashes (/) or raw strings to avoid escape sequence issues in Windows.

2. The script uses: 
python-docx for .docx files
PyMuPDF (fitz) for .pdf files


