import os
from datetime import date, timedelta

# Configuration
BRIEFS_DIR = "daily-briefs"
os.makedirs(BRIEFS_DIR, exist_ok=True)

def fetch_and_filter_articles():
    # TODO: expand with real RSS/Medium/Substack fetch/summarize
    # Example static data; replace with your fetching code!
    return [
        {
            "title": "AI in Product Management: Trends for 2026",
            "url": "https://hbr.org/ai-pm-2026",
            "summary": "A look at how AI is reshaping the product management space, with predictions for the next year.",
        },
        {
            "title": "Using LLMs to Build Better Product Roadmaps",
            "url": "https://a16z.com/building-roadmaps-with-llm",
            "summary": "LLMs can speed up product ideation and improve roadmapping—here's how.",
        }
    ]

def write_daily_brief(articles, brief_date):
    filename = f"{BRIEFS_DIR}/{brief_date}.html"
    title = f"AI Product Management Daily Brief – {brief_date}"
    items = [
        f"<h3><a href='{a['url']}' target='_blank'>{a['title']}</a></h3><p>{a['summary']}</p>"
        for a in articles
    ]
    content = f"""<html>
<head>
  <meta charset="utf-8">
  <title>{title}</title>
  <style>
    body {{ font-family: Arial, sans-serif; max-width: 700px; margin: auto; padding: 2em; }}
    h1, h3 {{ color: #274690; }}
    a {{ color: #2d85fd; text-decoration: none; }}
    a:hover {{ text-decoration: underline; }}
    hr {{ margin: 2em 0; }}
  </style>
</head>
<body>
  <a href="../index.html">&larr; Back to Main Index</a>
  <h1>{title}</h1>
  <hr />
  {''.join(items) if items else '<p>No relevant articles found today.</p>'}
</body>
</html>
"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    return filename

def update_index(brief_dates):
    links = [
        f'<li><a href="daily-briefs/{d}.html">{d}</a></li>'
        for d in sorted(brief_dates, reverse=True)
    ]
    content = f"""<html>
<head>
  <meta charset="utf-8">
  <title>AI Product Management Daily Brief Dashboard</title>
  <style>
    body {{ font-family: Arial, sans-serif; max-width: 600px; margin: auto; padding: 2em; }}
    h1 {{ color: #274690; }}
    li {{ margin-bottom: 0.7em; }}
    a {{ color: #2d85fd; text-decoration: none; }}
    a:hover {{ text-decoration: underline; }}
  </style>
</head>
<body>
  <h1>AI Product Management Daily Brief Dashboard</h1>
  <p>Browse your daily summaries of the best AI and Product Management articles.</p>
  <ul>
    {''.join(links)}
  </ul>
</body>
</html>
"""
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(content)

def get_existing_brief_dates():
    if not os.path.exists(BRIEFS_DIR):
        return []
    files = [f for f in os.listdir(BRIEFS_DIR) if f.endswith('.html')]
    dates = [f.replace('.html', '') for f in files]
    return dates

if __name__ == "__main__":
    today = date.today().isoformat()
    articles = fetch_and_filter_articles()
    write_daily_brief(articles, today)
    dates = get_existing_brief_dates()
    update_index(dates)
