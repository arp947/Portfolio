import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

st.set_page_config(page_title="Arpit Singh | Portfolio", layout="wide")

# Sidebar
with st.sidebar:
    st.title("Arpit Singh")
    st.write("📧 arpitsinghiis25@gmail.com")
    st.write("🔗 [LinkedIn](https://www.linkedin.com/in/arpit-singh0369?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)")
    st.write("🐙 [GitHub](https://github.com/arp947)")
    st.write("💻 [LeetCode](https://leetcode.com/u/aDMzDu12ES/)")

# Hero
st.title("Hi, I'm Arpit Singh 👋")
st.subheader("Aspiring AI/ML Engineer | Data Science Enthusiast")
st.write(
    "Motivated Computer engineering student with knowledge of Machine Learning, Deep Learning fundamentals and Data Science. "
    "Skilled in developing practical projects and eager to contribute to innovative AI-driven solutions "
    "while expanding expertise in modern AI technologies."
)

st.divider()

# Education
st.header("🎓 Education")
st.write("**ABES Engineering College** — Electrical and Computer Engineering (Sept 2024 – July 2028)")


st.divider()

# Skills
st.header("🛠️ Skills")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.subheader("Languages")
    st.write("Python, Java (DSA), SQL")
with col2:
    st.subheader("Data Science & ML")
    st.write("NumPy, Pandas, Scikit-Learn, Data Preprocessing, Feature Engineering, Model Evaluation, Matplotlib, Seaborn")
with col3:
    st.subheader("Deep Learning")
    st.write("PyTorch, ANN, Computer Vision, NLP")
with col4:
    st.subheader("Technologies")
    st.write("Streamlit, Flask, Agno")
    st.subheader("Core Subjects")
    st.write("DSA, OOP, DBMS")

st.divider()

# Projects
st.header("🚀 Projects")

projects = [
    {
        "title": "Snap Class",
        "link": "https://snapclass-frontend.onrender.com/",
        "points": [
            "Developed a full-stack web app using Python and Streamlit for automated classroom attendance.",
            "Implemented face recognition using dlib and a trained SVM classifier to identify students from classroom photos.",
            "Integrated voice biometrics using Resemblyzer for voice-based attendance marking.",
            "Used Supabase (PostgreSQL) as the backend database for storing student profiles, subjects and attendance logs.",
            "Deployed the main application on Streamlit Cloud and the landing page on Render.",
        ],
        "stack": "Python, Streamlit, dlib, scikit-learn, Resemblyzer, Supabase, PostgreSQL, Render",
    },
    {
        "title": "AI Resume ATS System",
        "link": "https://ats-scorer-ywvvakn5qqdi6dojymh2dj.streamlit.app/",
        "points": [
            "Developed a full-stack AI resume analyzer utilizing NLP to parse complex PDF layouts, improving text extraction accuracy by 15% over standard parsers.",
            "Implemented keyword extraction and semantic similarity analysis using spaCy and SentenceTransformers to generate ATS compatibility scores.",
            "Integrated Groq LLM to provide personalized resume feedback and improvement suggestions.",
            "Developed REST API using FastAPI with JWT-based authentication via Supabase.",
            "Built an interactive frontend using Streamlit with user history tracking and PDF report generation.",
            "Deployed backend on Hugging Face Spaces (Docker) and frontend on Streamlit Community Cloud.",
        ],
        "stack": "Python, FastAPI, spaCy, SentenceTransformers, Groq LLM, PyJWT, WeasyPrint, pdfplumber, python-docx, Streamlit, Supabase",
    },
    {
        "title": "AI Real-time Gym Coach",
        "link": "https://soft-lily-911d8b.netlify.app/##contact",
        "points": [
            "Built an AI-powered gym coaching web app using Python and Streamlit with real-time pose detection via MediaPipe.",
            "Integrated Groq LLM API for natural language fitness coaching and personalized workout recommendations.",
            "Implemented real-time video processing with OpenCV and WebRTC for live exercise form analysis.",
            "Added text-to-speech feedback using gTTS to provide audio cues during workouts.",
        ],
        "stack": "Python, Streamlit, MediaPipe, OpenCV, WebRTC, Groq LLM API, gTTS, Pandas",
    },
]

for project in projects:
    with st.expander(f"**{project['title']}**"):
        for point in project["points"]:
            st.write(f"- {point}")
        st.write(f"**Tech Stack:** {project['stack']}")
        st.markdown(f"[🔗 View Project]({project['link']})")

st.divider()

# Contact
st.header("📬 Contact Me")

SENDER_EMAIL = "arpitsinghiis25@gmail.com"
SENDER_PASSWORD = st.secrets["email_password"] if "email_password" in st.secrets else ""

with st.form("contact"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    if st.form_submit_button("Send"):
        if not name or not email or not message:
            st.warning("Please fill in all fields.")
        elif not SENDER_PASSWORD:
            st.error("Email password not configured. Add it to .streamlit/secrets.toml")
        else:
            try:
                msg = MIMEMultipart()
                msg["From"] = SENDER_EMAIL
                msg["To"] = SENDER_EMAIL
                msg["Subject"] = f"Portfolio Contact from {name}"
                body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
                msg.attach(MIMEText(body, "plain"))

                with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                    server.login(SENDER_EMAIL, SENDER_PASSWORD)
                    server.sendmail(SENDER_EMAIL, SENDER_EMAIL, msg.as_string())

                st.success("✅ Message sent! I'll get back to you soon.")
            except Exception as e:
                st.error(f"Failed to send message: {e}")
