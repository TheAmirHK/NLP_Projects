import os
import openai
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

print("\n\nBot: What is the email you want to check ?")
while True:
    user_input = input("")
    if user_input == "exit" or user_input == "quit":
        break
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an email spam or ham detector. User will send you an email and then you only tell them This emai is REAL or This email is SPAM !"},
            {"role": "user", "content": user_input}
        ],
        temperature=1,
        max_tokens=150,
    )

    response_message = response["choices"][0]["message"]
    response_content = response_message["content"]

    print("Bot:" + response_content)
