# Local-LLM-Deployment-and-Interaction

This script demonstrates how to interact with a local LLM (Large Language Model) server using the curl command. It also explains how to handle the output and extract meaningful information from the model's responses.

Prerequisites:
Before running this script, ensure you have the following installed:

Python 3.x
curl command-line tool

Setup Instructions:

I have downloaded the LLM server repository that includes the Phi3, gemma:2b model using ollama run phi3 and ollama run gemma:2b locally.

Then I startd the LLM server on your local machine. We can typically start it by running a command like ./start_server.sh or similar, as mentioned in the server's documentation.

Script Explanation :
The provided Python script which are two files here interacts with the LLM server using the curl command. Here's how it works:

Define the curl command with the appropriate arguments to send a message to the LLM server:


curl http://localhost:11434/api/chat -d '{"model": "phi3", "messages": [{ "role": "user", "content": "what is stock market?" }]}'
Execute the curl command using Python's subprocess module.


curl http://localhost:11434/api/chat -d '{"model": "gemma:2b", "messages": [{ "role": "user", "content": "what is stock market?" }]}'
Execute the curl command using Python's subprocess module.

Process the output received from the LLM server:

The script splits the output into lines and processes each line as a separate JSON object.
It extracts the content of the messages from the JSON response.
Print the extracted sentence obtained from the LLM server's response.

Running the Script:

We have to mak sure the LLM server with the Phi3/gemma:2b model is running locally on your machine.
Execute the Python script using:
Copy code
python gemma2b.py/ phi3.py

Additional Notes:

The difference in output between the two models, Phi3 and Gemma:2b, is likely due to several factors:

Model Architecture: Each model is trained on different datasets and uses a distinct architecture for processing and generating responses. This can result in variations in the way they interpret and respond to input prompts.

Training Data: The training data for each model may cover different topics, contexts, and linguistic nuances. This can influence how the models understand and generate responses related to specific queries like the explanation of Rayleigh scattering.

Scoring and Optimization: Models like Phi3 and Gemma:2b may prioritize different aspects of response generation, such as accuracy, coherence, relevance, or language fluency. These priorities can lead to differences in the generated content.

Parameter Tuning: The parameters and configurations used during model training and deployment can impact the model's behavior and the quality of its responses.
