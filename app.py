import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="AI DevOps Copilot", layout="centered")

st.title("AI DevOps Copilot (Chat Mode)")

st.subheader("Upload Log File")

uploaded_file = st.file_uploader("Upload your log file", type=["txt", "log"])

if uploaded_file:
    log_content = uploaded_file.read().decode("utf-8")

    st.text_area("Uploaded Logs", log_content, height=200)

    if st.button("Auto Analyze Uploaded Logs"):
        with st.spinner("Analyzing uploaded logs..."):
            messages = [
                {"role": "system", "content": "You are an expert DevOps SRE assistant."},
                {"role": "user", "content": f"Analyze these logs:\n{log_content}"}
            ]

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages
            )

            result = response.choices[0].message.content

            st.subheader("Analysis Result")
            st.write(result)

            # Download as TXT
            st.download_button(
                label="Download Report (TXT)",
                data=result,
                file_name="devops_analysis.txt",
                mime="text/plain"
             )
        import json

        json_data = json.dumps(result, indent=2)

        st.download_button(
            label="📥 Download JSON",
            data=json_data,
            file_name="analysis.json",
            mime="application/json"
        )

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
user_input = st.chat_input("Ask about your logs or DevOps issue...")

if user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.write(user_input)

    # Prepare messages for AI
    messages = [
        {"role": "system", "content": "You are an expert DevOps SRE assistant."}
    ] + st.session_state.messages

    # AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages
            )

            reply = response.choices[0].message.content
            st.write(reply)

    # Save AI response
    st.session_state.messages.append({"role": "assistant", "content": reply})
