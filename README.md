# 🚀 AI DevOps Copilot

## Live Demo
[Try the app here](https://ai-devops-copilot.streamlit.app)

## Source Code
[View the GitHub Repository](https://github.com/Manikumargadi/ai-devops-copilot)

---

## Overview
AI DevOps Copilot is a live AI-powered assistant built to help engineers analyze infrastructure and deployment logs, identify root causes, classify incident severity, and recommend actionable fixes.

Instead of manually scanning raw logs, users can upload log files or ask troubleshooting questions through a chat interface. The tool helps speed up debugging and makes incident investigation more structured and efficient.

---

## Why I Built This
In real DevOps and SRE workflows, debugging infrastructure issues often means spending a lot of time manually reading logs, identifying patterns, and figuring out next steps. I built this project to simplify that process by combining AI-driven analysis with a clean interactive interface.

The goal was to create a practical tool that feels useful in real-world operations, especially for troubleshooting Kubernetes failures, CI/CD pipeline issues, resource bottlenecks, and cloud infrastructure problems.

---

## Key Features
- 📂 Upload `.log` or `.txt` files for analysis
- 🧠 Detect root causes from infrastructure and deployment logs
- 🚨 Classify severity levels such as Critical, Warning, and Info
- 💬 Chat with an AI DevOps assistant for follow-up troubleshooting
- 📥 Download analysis reports as TXT or JSON
- 🎨 Clean web interface built with Streamlit
- 🔒 Session-based request limiting for safer API usage

---

## Sample Use Cases
This project can be used for scenarios like:
- Kubernetes pod crashes such as `OOMKilled`
- High CPU or memory usage alerts
- Database connection timeouts
- CI/CD pipeline failures
- Docker container runtime issues
- VPC or networking misconfigurations
- General cloud incident investigation

---

## Example Workflow
1. Upload a log file through the web app
2. The AI analyzes the log contents
3. The app returns:
   - Issue Summary
   - Root Cause
   - Severity
   - Recommended Fix
4. Ask follow-up questions in chat mode
5. Download the final analysis as TXT or JSON

---

## Architecture
```text
User
  ↓
Streamlit Web UI
  ↓
OpenAI API
  ↓
Log Analysis + Severity Detection + Recommendations
  ↓
Structured Output + Downloadable Report

## Screenshots

### Home Page
Shows the main interface with request tracking, log upload, and chat assistant.

<img width="947" height="736" alt="screenshots:home" src="https://github.com/user-attachments/assets/9e42215e-52d7-4613-b51f-3018f2676842" />


### Log Upload Workflow
Example of uploading an infrastructure log file before running automated analysis.

<img width="850" height="742" alt="screenshots:upload" src="https://github.com/user-attachments/assets/c8ce0ca5-e64a-4988-9f1e-232e9f743ebf" />


### AI Analysis Result
Structured output including issue summary, root cause, severity, recommended fix, and downloadable reports.

<img width="828" height="636" alt="screenshots:analysis" src="https://github.com/user-attachments/assets/331c965c-2226-4eae-be2d-e5a871a207ed" />


