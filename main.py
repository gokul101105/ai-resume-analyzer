import streamlit as st
from dotenv import load_dotenv
import os
import PyPDF2
import io
import time
from google import genai

# Load environment variables
load_dotenv()

st.set_page_config(
    page_title="AI Resume Analyser",
    page_icon="📃",
    layout="centered"
)

st.title(" AI Resume Analyser")
st.markdown("Upload your resume in **PDF** or **TXT** format and let AI analyze it.")

# Load Gemini API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    st.error(" GEMINI_API_KEY not found in .env file.")
    st.stop()

client = genai.Client(api_key=GEMINI_API_KEY)

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf", "txt"]
)

job_role = st.text_input(
    "Job Role",
    placeholder="Example: Java Full Stack Developer"
)

analyze = st.button(" Analyze Resume")


def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""

    for page in pdf_reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    return text


def extract_text(uploaded_file):
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(io.BytesIO(uploaded_file.read()))
    else:
        return uploaded_file.read().decode("utf-8")


if analyze:

    if uploaded_file is None:
        st.error("Please upload your resume.")
        st.stop()

    try:
        resume_text = extract_text(uploaded_file)

        if not resume_text.strip():
            st.error("No readable text found in the file.")
            st.stop()

        prompt = f"""
You are an expert HR Recruiter and ATS Resume Reviewer.

Analyze this resume for the role:

{job_role if job_role else "Software Engineer"}

Provide your response in markdown with the following sections:

# Overall Resume Score (out of 100)

# ATS Compatibility Score (out of 100)

# Strengths

# Weaknesses

# Missing Skills

# Suggestions for Improvement

# Recommended Projects

# Final Verdict

Resume:

{resume_text}
"""

        with st.spinner("Analyzing Resume..."):

            response = None

            for attempt in range(3):
                try:
                    response = client.models.generate_content(
                        model="gemini-2.5-flash",
                        contents=prompt
                    )
                    break

                except Exception as e:

                    if "503" in str(e):
                        st.warning(
                            f"Gemini server is busy. Retrying ({attempt+1}/3)..."
                        )
                        time.sleep(5)
                    else:
                        raise e

        if response is None:
            st.error(
                "Gemini servers are currently busy.\n\nPlease try again after a few minutes."
            )
            st.stop()

        st.success("Resume Analysis Completed!")

        st.markdown("---")
        st.markdown(response.text)

    except Exception as e:
        st.error(f" Error:\n\n{e}")