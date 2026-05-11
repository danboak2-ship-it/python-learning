from flask import Flask, request, jsonify, render_template
import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate_email():
    data = request.json
    bullet_points = data["bullet_points"]
    tone = data["tone"]
    
    message = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": f"Write a professional email based on these bullet points: {bullet_points}. Tone should be: {tone}"}
        ]
    )
    
    return jsonify({"email": message.content[0].text})

if __name__ == "__main__":
    app.run(debug=True)