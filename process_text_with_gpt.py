import os
import openai

# Initialize OpenAI API with your API key
openai.api_key = 'YOUR API'

# Define the function to process text through GPT-4
def process_text_with_gpt(text):
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an expert working with .php files to correct grammar, spelling, and improving readability in British English. Do not add code blocks, comments, explanations, or any extra content other than the corrected PHP code."},
            {"role": "user", "content": f"Here is a Laravel blade code, Please correct the following text for grammar, spelling, and readability without adding any additional information or context:\n\n{text}"}
        ]
    )
    return response['choices'][0]['message']['content']

# Use the current working directory
current_directory = os.getcwd()

# Loop through each file in the current directory
for filename in os.listdir(current_directory):
    if filename.endswith(".php"):  # Only process .php files
        input_filepath = os.path.join(current_directory, filename)
        
        # Open and read the input file
        with open(input_filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Process the content using GPT-4
        corrected_content = process_text_with_gpt(content)
        
        # Write the corrected content back to the original file
        with open(input_filepath, 'w', encoding='utf-8') as output_file:
            output_file.write(corrected_content)
        
        print(f"Processed and saved {filename}")

print("All .php files in the current folder have been processed.")
