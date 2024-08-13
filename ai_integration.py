import openai

# Use your actual API key
openai.api_key = "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"

def generate_code(user_prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI code generator."},
            {"role": "user", "content": user_prompt}
        ]
    )
    return response.choices[0].message["content"].strip()

# Example prompt
user_prompt = "Write a Python script that prints 'Hello, World!'"

# Generate the code
generated_code = generate_code(user_prompt)
print("Generated Code:\n", generated_code)
