import os
from openai import OpenAI


def analyze_logs(log_text):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
prompt = f"""
Return output in JSON format:

{{
  "issue": "...",
  "root_cause": "...",
  "severity": "...",
  "fix": "..."
}}

Logs:
{log_text}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
