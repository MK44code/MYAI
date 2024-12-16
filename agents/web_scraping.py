
import trafilatura
from transformers import pipeline

def ai_web_scraper(url, query):
    try:
        downloaded = trafilatura.fetch_url(url)
        content = trafilatura.extract(downloaded)
        if not content:
            return "Failed to extract content using AI scraping."

        summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        prompt = f"{content[:4000]} \nSummarize the above content focusing on: {query}"
        summary = summarizer(prompt, max_length=130, min_length=30, do_sample=False)[0]['summary_text']

        return summary
    except Exception as e:
        return f"Error occurred: {str(e)}"
