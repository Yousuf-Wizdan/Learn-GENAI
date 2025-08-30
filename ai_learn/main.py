from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.environ.get("API_KEY")

client = OpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {   
            "role": "system",
            "content": "You are expert in Maths only answer math question"
        },
        {
            "role": "user",
            "content": "Hey, I am Yousuf! Nice to Meet YOU"
        }
    ]
)

print(response.choices[0].message.content)