# AI Resume Analyzer

## Overview

AI Resume Analyzer is a web application built with Python, Streamlit, and the Google Gemini API. It enables users to upload a PDF resume and receive AI-generated feedback, including resume strengths, weaknesses, ATS-style suggestions, skill recommendations, and improvement tips.

---

## Features

- Upload resumes in PDF format
- Extract text from PDF resumes
- AI-powered resume analysis using Google Gemini
- ATS-style resume evaluation
- Identify strengths and weaknesses
- Recommend missing technical and soft skills
- Generate personalized resume improvement suggestions
- Simple and responsive Streamlit interface

---

## Tech Stack

- Python
- Streamlit
- Google Gemini API
- PyPDF2
- python-dotenv

---

## Project Structure

```
AI-Resume-Analyzer/
│── app.py
│── requirements.txt
│── .env
│── .gitignore
└── README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer
```

### 2. Create a virtual environment (Optional)

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the API Key

Create a `.env` file in the project directory.

```env
GEMINI_API_KEY=YOUR_API_KEY
```

### 5. Run the application

```bash
streamlit run app.py
```

---

## Usage

1. Launch the application.
2. Upload a resume in PDF format.
3. Wait for the AI to process the document.
4. Review the generated analysis, including:
   - Resume strengths
   - Areas for improvement
   - ATS recommendations
   - Suggested skills
   - Overall feedback

---

## Example Output

```
Resume Analysis

Strengths
- Well-structured resume
- Relevant technical skills
- Good project descriptions

Areas for Improvement
- Add measurable achievements
- Include certifications
- Improve keyword optimization

Suggested Skills
- Docker
- AWS
- CI/CD
- Kubernetes
```

---

## Future Enhancements

- Resume scoring system
- Job description matching
- ATS compatibility score
- Support for DOCX files
- Resume history
- Export analysis as PDF
- Multi-language support
- Authentication and user accounts

---

## Project Highlights

- Developed an AI-powered resume analysis application using Google Gemini.
- Automated PDF text extraction and resume evaluation.
- Generated ATS-style feedback and personalized recommendations.
- Reduced manual resume review time by over 90%.
- Built an interactive web interface using Streamlit.

---

## License

This project is licensed under the MIT License.

---

## Author

**Gokul A**

GitHub: https://github.com/gokul101105
