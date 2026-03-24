from flask import Flask, render_template, request, jsonify
from scraper import scrape_url
from openai import OpenAI
from dotenv import load_dotenv
from flask_cors import CORS
import os
load_dotenv(override=True)

app = Flask(__name__)
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url="https://api.openai.com/v1"
)

def summarize(text, style):
    prompts = {
        "bullets": "Summarize this article in 5 clear bullet points. Be concise.",
        "short":   "Give a 2-3 sentence summary of this article. Very brief.",
        "detailed":"Give a detailed summary covering all key points of this article.",
        "eli5":    "Explain this article like I'm 5 years old. Simple words only."
    }
    instruction = prompts.get(style, prompts["bullets"])


    response = client.chat.completions.create(
        model= "gpt-oss:120b-cloud" ,
        messages=[
            {"role": "system", "content": "You are a professional news summarizer. Read the article content and summarize it clearly and accurately."},
            {"role": "user",   "content": f"{instruction}\n\nArticle content:\n{text[:3000]}"}
        ],
        max_tokens = 4000,
        temperature=0
    )
    return response.choices[0].message.content

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/summarize", methods=["POST"])
def handle_summarize():
    data = request.json
    url   = data.get("url", "").strip()
    style = data.get("style", "bullets")

    if not url:
        return jsonify({"error": "Please enter a URL"}), 400

    try:
        scraped = scrape_url(url)
        
        if not scraped["text"]:
            return jsonify({"error": "Could not extract content from this URL"}), 400

        summary = summarize(scraped["text"], style)
        print(summary)
        return jsonify({
            "title":   scraped["title"],
            "summary": summary,
            "words":   len(scraped["text"].split())
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)