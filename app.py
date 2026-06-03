import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
import os
import json

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

try:
    if not api_key:
        api_key = st.secrets["OPENAI_API_KEY"]
except Exception:
    pass

client = OpenAI(api_key=api_key)

# Page config
st.set_page_config(
    page_title="AI DevOps Copilot",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Session state
if "request_count" not in st.session_state:
    st.session_state.request_count = 0

if "messages" not in st.session_state:
    st.session_state.messages = []

MAX_REQUESTS = 5

# Light theme styling
st.markdown("""
<style>
.stApp {
    background-color: #f7f9fc;
    color: #1f2937;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

.card {
    padding: 15px;
    border-radius: 12px;
    background-color: white;
    margin-bottom: 12px;
    color: #111827;
    border: 1px solid #e5e7eb;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}

.critical { border-left: 5px solid #ef4444; }
.warning { border-left: 5px solid #f59e0b; }
.info { border-left: 5px solid #10b981; }

h1, h2, h3, h4, p, label, div {
    color: #111827 !important;
}

[data-testid="stChatMessage"] {
    background-color: white;
    color: #111827;
    border-radius: 12px;
    padding: 12px;
    border: 1px solid #e5e7eb;
    margin-bottom: 10px;
}

[data-testid="stTextArea"] textarea,
[data-testid="stTextInput"] input {
    background-color: white !important;
    color: #111827 !important;
}

[data-testid="stFileUploader"] {
    background-color: white;
    border-radius: 12px;
    padding: 10px;
    border: 1px solid #e5e7eb;
}

div.stButton > button {
    background-color: #2563eb;
    color: white;
    border-radius: 10px;
    border: none;
    padding: 0.6rem 1rem;
    font-weight: 600;
}

div.stButton > button:hover {
    background-color: #1d4ed8;
    color: white;
}

[data-testid="stDownloadButton"] > button {
    border-radius: 10px;
}

.request-box {
    background-color: #eef4ff;
    border: 1px solid #dbeafe;
    padding: 12px;
    border-radius: 10px;
    margin-bottom: 20px;
    color: #1e3a8a;
    font-weight: 500;
}
</style>
""", unsafe_allow_html=True)

# Output formatter
def format_output(result: str) -> None:
    sections = result.split("\n")

    for line in sections:
        line = line.strip()

        if not line:
            continue

        if "Severity" in line:
            if "Critical" in line:
                st.markdown(f"<div class='card critical'>🚨 <b>{line}</b></div>", unsafe_allow_html=True)
            elif "Warning" in line:
                st.markdown(f"<div class='card warning'>⚠️ <b>{line}</b></div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='card info'>✅ <b>{line}</b></div>", unsafe_allow_html=True)

        elif "Issue Summary" in line:
            st.markdown(f"<div class='card'><b>📌 {line}</b></div>", unsafe_allow_html=True)

        elif "Root Cause" in line or "Likely Root Cause" in line:
            st.markdown(f"<div class='card'><b>🧠 {line}</b></div>", unsafe_allow_html=True)

        elif "Recommended Fix" in line:
            st.markdown(f"<div class='card'><b>🛠️ {line}</b></div>", unsafe_allow_html=True)

        elif "Kubernetes Checks" in line:
            st.markdown(f"<div class='card'><b>✅ {line}</b></div>", unsafe_allow_html=True)

        elif "Suggested kubectl Commands" in line:
            st.markdown(f"<div class='card'><b>💻 {line}</b></div>", unsafe_allow_html=True)

        elif "Runbook Steps" in line:
            st.markdown(f"<div class='card'><b>📋 {line}</b></div>", unsafe_allow_html=True)

        else:
            st.markdown(f"<div class='card'>{line}</div>", unsafe_allow_html=True)

# Header
st.markdown("<h1 style='text-align:center;'>🚀 AI DevOps Copilot</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:18px;'>Analyze logs. Detect issues. Fix faster.</p>", unsafe_allow_html=True)

# Request counter
st.markdown(
    f"<div class='request-box'>Requests used: {st.session_state.request_count}/{MAX_REQUESTS}</div>",
    unsafe_allow_html=True
)

# -------------------------------
# Upload Log Analysis Section
# -------------------------------
st.subheader("📂 Upload Log File")

uploaded_file = st.file_uploader("Upload your log file", type=["txt", "log"])

if uploaded_file:
    log_content = uploaded_file.read().decode("utf-8")
    st.text_area("📄 Uploaded Logs", log_content, height=200)

    if st.button("⚡ Auto Analyze Uploaded Logs"):
        if st.session_state.request_count >= MAX_REQUESTS:
            st.error("Usage limit reached for this session.")
            st.stop()

        with st.spinner("Analyzing logs..."):
            prompt = f"""
Analyze these logs and return output in this format:

Issue Summary: <short summary>
Root Cause: <root cause>
Severity: <Critical/Warning/Info>
Recommended Fix: <fix>

Logs:
{log_content}
"""

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )

            st.session_state.request_count += 1
            result = response.choices[0].message.content

            st.subheader("🧠 Analysis Result")
            format_output(result)

            st.download_button(
                label="📥 Download TXT",
                data=result,
                file_name="analysis.txt",
                mime="text/plain"
            )

            json_data = json.dumps({"analysis": result}, indent=2)

            st.download_button(
                label="📥 Download JSON",
                data=json_data,
                file_name="analysis.json",
                mime="application/json"
            )

# -------------------------------
# Kubernetes Troubleshooting Agent
# -------------------------------
st.subheader("☸️ Kubernetes Troubleshooting Agent")

k8s_issue = st.selectbox(
    "Select Kubernetes issue type",
    [
        "CrashLoopBackOff",
        "OOMKilled",
        "ImagePullBackOff",
        "Pending Pod",
        "Service / DNS Issue",
        "Deployment Failure"
    ]
)

k8s_input = st.text_area(
    "Paste pod logs, kubectl describe output, or Kubernetes error message",
    height=200,
    key="k8s_input"
)

if st.button("🔍 Analyze Kubernetes Issue"):
    if st.session_state.request_count >= MAX_REQUESTS:
        st.error("Usage limit reached for this session.")
        st.stop()

    if k8s_input.strip():
        with st.spinner("Analyzing Kubernetes issue..."):
            prompt = f"""
You are an expert Kubernetes SRE assistant.

The user is facing this Kubernetes issue type:
{k8s_issue}

Here is the Kubernetes input:
{k8s_input}

Return output in this format:

Issue Summary: <short summary>
Likely Root Cause: <root cause>
Kubernetes Checks: <what to verify>
Suggested kubectl Commands: <commands to run>
Recommended Fix: <recommended fix>
Runbook Steps:
1. <step 1>
2. <step 2>
3. <step 3>
"""

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )

            st.session_state.request_count += 1
            k8s_result = response.choices[0].message.content

            st.subheader("☸️ Kubernetes Analysis Result")
            format_output(k8s_result)

            st.download_button(
                label="📥 Download Kubernetes Report",
                data=k8s_result,
                file_name="kubernetes_analysis.txt",
                mime="text/plain"
            )
    else:
        st.warning("Please paste Kubernetes logs or error details.")

# -------------------------------
# Chat Section
# -------------------------------
st.subheader("💬 Chat with DevOps Assistant")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Ask DevOps questions...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            if st.session_state.request_count >= MAX_REQUESTS:
                st.error("Usage limit reached for this session.")
                st.stop()

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=st.session_state.messages
            )

            st.session_state.request_count += 1
            reply = response.choices[0].message.content
            st.write(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
