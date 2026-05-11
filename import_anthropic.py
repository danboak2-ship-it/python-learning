import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

def summarise(text):
    message = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": f"Summarise this in 2-3 sentences: {text}"}
        ]
    )
    return message.content[0].text

user_input = input("Paste your text here: ")
result = summarise(user_input)
print("\nSummary:")
print(result)