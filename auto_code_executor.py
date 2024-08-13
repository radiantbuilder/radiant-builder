import openai
import os
import logging

# Initialize OpenAI API key
openai.api_key = "your-openai-api-key"

def generate_code(user_prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an advanced AI capable of handling complex coding tasks. Please ensure all code is efficient and follows best practices."},
            {"role": "user", "content": user_prompt}
        ],
        max_tokens=500  # Increase the token limit for more complex tasks
    )
    return response['choices'][0]['message']['content'].strip()

def save_and_execute_code(code, file_name="generated_script.py"):
    with open(file_name, "w") as code_file:
        code_file.write(code)
    logging.info(f"Code saved to {file_name}")

    try:
        exec(open(file_name).read())
        logging.info(f"Code executed successfully from {file_name}.")
    except Exception as e:
        logging.error(f"Error executing code: {e}")

def main():
    logging.basicConfig(filename="auto_code_executor.log", level=logging.INFO)

    # Example prompts for more complex tasks
    prompts = [
        "Write a Python script that connects to a database, retrieves data, and prints it out.",
        "Create a Python function that performs sentiment analysis on text using a pre-trained model.",
        "Build a basic web scraper using Python that extracts titles from a webpage."
    ]

    for user_prompt in prompts:
        logging.info(f"Generating code for prompt: {user_prompt}")
        generated_code = generate_code(user_prompt)
        logging.info("Code generated successfully.")

        if generated_code:
            save_and_execute_code(generated_code)
        else:
            logging.error("No code to save or execute.")

if __name__ == "__main__":
    main()
