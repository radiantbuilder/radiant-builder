import openai

openai.api_key = "your-openai-api-key"

prompt = "Create a Python script that monitors CPU usage and alerts if it exceeds 90%."

response = openai.Completion.create(
    engine="davinci-codex",
    prompt=prompt,
    max_tokens=150
)

script = response.choices[0].text.strip()

with open("cpu_monitor.py", "w") as f:
    f.write(script)
