import os
import sys
import openai

# Load your API key from an environment variable or secret management service
root_dir = dir = os.path.dirname(sys.argv[0])
openai.api_key_path = f"{root_dir}/helion.key"

#chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
#print(chat_completion)