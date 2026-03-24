# NewsBrief — AI News Summarizer

A web app that scrapes any news article or webpage and summarizes it using a **local LLM via Ollama** — completely free, no API costs, runs 100% on your machine.

---

Screenshots
Home — paste any article URL

![NewsBrief Home](screenshots/home.png)

Summarizing news by local llm (gpt-oss-safeguard)

![NewsBrief Home](screenshots/loading.png)

Result — AI-generated summary

![NewsBrief result](screenshots/result.png)

## Features

- Paste any article URL and get an instant summary
- 4 summary styles — bullet points, quick, detailed, explain simply
- Powered by your local Ollama model (no OpenAI costs)
- Clean newspaper-style UI
- Works with Wikipedia, news sites, blogs, and more

---

## Tech Stack

- **Backend** — Python, Flask
- **Scraping** — requests, BeautifulSoup4
- **LLM** — Ollama (local) via OpenAI-compatible API
- **Frontend** — HTML, CSS, vanilla JavaScript

---

## Requirements

- Python 3.10+
- [Ollama](https://ollama.com) installed and running
- A pulled Ollama model (e.g. `llama3.2`, `mistral`)

---

## Setup

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/news-summarizer.git
cd news-summarizer
```

### 2. Install dependencies

```bash
# Using uv (recommended)
uv init
uv add flask requests beautifulsoup4 openai python-dotenv

# Or using pip
pip install -r requirements.txt
```

### 3. Configure environment

Create a `.env` file in the root folder:

```env
OPENAI_API_KEY=ollama
OPENAI_BASE_URL=http://localhost:11434/v1
MODEL_NAME=gpt-oss-safeguard:20b
```

Replace `MODEL_NAME` with whatever model you have. Check yours with:

```bash
ollama list
```

### 4. Start Ollama

Make sure Ollama is running with your model:

```bash
ollama run gpt-oss-safeguard:20b
```

### 5. Run the app

```bash
# Using uv
uv run main.py

# Or using python
python main.py
```

Open your browser at `http://localhost:5000`

---

## Project Structure

```
news-summarizer/
├── main.py               # Flask backend + LLM integration
├── scraper.py            # Web scraping logic
├── .env                  # Environment variables (not committed)
├── requirements.txt      # Python dependencies
└── templates/
    └── index.html        # Frontend UI
```

---

## How It Works

```
Browser → Flask (port 5000) → scraper.py scrapes URL
                            → text sent to Ollama (port 11434)
                            → LLM generates summary
                            → summary returned to browser
```

1. User pastes a URL and selects summary style
2. Flask scrapes the article using `requests` + `BeautifulSoup`
3. Cleaned text is sent to local Ollama model
4. Summary is returned and displayed in the browser

---

## Summary Styles

| Style          | Description                |
| -------------- | -------------------------- |
| Bullet points  | 5 clear bullet points      |
| Quick summary  | 2-3 sentence overview      |
| Detailed       | Full comprehensive summary |
| Explain simply | ELI5 — simple words only   |

---

## Example URLs to Try

- `https://en.wikipedia.org/wiki/Artificial_intelligence`
- `https://en.wikipedia.org/wiki/Python_(programming_language)`
- `https://en.wikipedia.org/wiki/Large_language_model`

---

## Switching to OpenAI (optional)

To use real OpenAI instead of local Ollama, update your `.env`:

```env
OPENAI_API_KEY=sk-your-real-key-here
OPENAI_BASE_URL=
MODEL_NAME=gpt-4o
```

---

## Local vs Cloud LLM

|                 | Local (Ollama)      | Cloud (OpenAI) |
| --------------- | ------------------- | -------------- |
| Cost            | Free                | Paid per token |
| Privacy         | 100% local          | Sent to OpenAI |
| Speed           | Depends on hardware | Fast           |
| Internet needed | No                  | Yes            |

---

## Contributing

Pull requests are welcome! For major changes please open an issue first.

---
