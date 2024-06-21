import subprocess
import json

# Define the curl command as a list of arguments
curl_command = [
    'curl',
    'http://localhost:11434/api/chat',
    '-d', '{"model": "gemma:2b", "messages": [{ "role": "user", "content": "why is the sky blue?" }]}'
]

# Execute the curl command using subprocess
try:
    result = subprocess.run(curl_command, capture_output=True, text=True)
    output = result.stdout

    # Split the output into lines and process each line as a separate JSON object
    lines = output.strip().split('\n')
    sentences = []
    for line in lines:
        try:
            json_output = json.loads(line)
            if 'message' in json_output and 'content' in json_output['message']:
                sentences.append(json_output['message']['content'])
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")

    # Form a sentence from the extracted content
    sentence = ' '.join(sentences)
    print("Extracted Sentence:")
    print(sentence)

except subprocess.CalledProcessError as e:
    print(f"Error executing curl command: {e}")
