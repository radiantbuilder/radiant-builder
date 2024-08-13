import openai
import logging
import os  # Including this in case you need it later
from flask import Flask, request, render_template  # Including the necessary Flask imports

# Initialize OpenAI API key
import os  # Ensure this is at the top of your script with the other imports
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

def generate_code(user_prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an advanced AI capable of handling complex coding tasks. Please ensure all code is efficient and follows best practices."},
            {"role": "user", "content": user_prompt}
        ],
        max_tokens=500
    )
    return response['choices'][0]['message']['content'].strip()

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_prompt = request.form["prompt"]
        generated_code = generate_code(user_prompt)
        output = execute_code(generated_code)
        return render_template("index.html", code=generated_code, output=output)
    return render_template("index.html", code="", output="")

def execute_code(code, file_name="generated_script.py"):
    with open(file_name, "w") as code_file:
        code_file.write(code)
    logging.info(f"Code saved to {file_name}")

    try:
        exec(open(file_name).read())
        logging.info(f"Code executed successfully from {file_name}.")
        return "Code executed successfully."
    except Exception as e:
        logging.error(f"Error executing code: {e}")
        return f"Error executing code: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
