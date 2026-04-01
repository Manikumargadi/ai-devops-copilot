import os
from dotenv import load_dotenv
from services.log_reader import read_logs
from agents.log_analyzer import analyze_logs

# Load API key
load_dotenv()

if __name__ == "__main__":
    print("AI DevOps Copilot\n")

    logs = read_logs("sample_logs/error.log")

    print("Logs:\n", logs)

    result = analyze_logs(logs)

    print("\n Analysis:\n")
    print(result)
