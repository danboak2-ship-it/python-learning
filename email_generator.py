import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

def generate_email(bullet_points, tone):
    message = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": f"Write a professional email based on these bullet points: {bullet_points}. Tone should be: {tone}"}
        ]
    )
    return message.content[0].text

while True:
    bullet_points = input("\nEnter your bullet points (or 'quit' to exit): ")
    if bullet_points.lower() == "quit":
        break
    tone = input("Enter tone (formal/friendly/urgent): ")
    result = generate_email(bullet_points, tone)
    print("\nGenerated Email:")
    print(result)