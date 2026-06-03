# 🚀 AI DevOps Copilot

## Live Demo
[Try the app here](https://ai-devops-copilot.streamlit.app)

## Source Code
[View the GitHub Repository](https://github.com/Manikumargadi/ai-devops-copilot)

## Overview
AI DevOps Copilot is a live AI-powered assistant built to help engineers analyze infrastructure and deployment logs, identify root causes, classify incident severity, and recommend actionable fixes.

Instead of manually scanning raw logs, users can upload log files or ask troubleshooting questions through a chat interface. The tool helps speed up debugging and makes incident investigation more structured and efficient.

## Why I Built This
In real DevOps and SRE workflows, debugging infrastructure issues often means spending a lot of time manually reading logs, identifying patterns, and figuring out next steps. I built this project to simplify that process by combining AI-driven analysis with a clean interactive interface.

The goal was to create a practical tool that feels useful in real-world operations, especially for troubleshooting Kubernetes failures, CI/CD pipeline issues, resource bottlenecks, and cloud infrastructure problems.

## Key Features
- 📂 Upload `.log` or `.txt` files for analysis
- 🧠 Detect root causes from infrastructure and deployment logs
- 🚨 Classify severity levels such as Critical, Warning, and Info
- 💬 Chat with an AI DevOps assistant for follow-up troubleshooting
- ☸️ Troubleshoot Kubernetes issues like CrashLoopBackOff, OOMKilled, ImagePullBackOff, Pending Pods, and service/DNS failures
- 💻 Suggest relevant `kubectl` investigation commands
- 📋 Generate remediation-style runbook guidance
- 📥 Download analysis reports as TXT or JSON
- 🎨 Clean web interface built with Streamlit
- 🔒 Session-based request limiting for safer API usage

## Sample Use Cases
This project can be used for scenarios like:
- Kubernetes pod crashes such as `OOMKilled`
- `CrashLoopBackOff` and failed restarts
- `ImagePullBackOff` and container image issues
- Pending pods caused by insufficient resources
- Service or DNS connectivity failures inside Kubernetes
- Database connection timeouts
- CI/CD pipeline failures
- Docker container runtime issues
- VPC or networking misconfigurations
- General cloud incident investigation

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

## Kubernetes Troubleshooting Workflow
1. Select a Kubernetes issue type
2. Paste pod logs, `kubectl describe` output, or error details
3. The AI returns:
   - Issue Summary
   - Likely Root Cause
   - Kubernetes Checks
   - Suggested kubectl Commands
   - Recommended Fix
   - Runbook Steps
4. Download the troubleshooting report

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
