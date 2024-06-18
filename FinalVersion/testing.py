#import openai
from pygooglenews import GoogleNews
from newspaper import Article
import nltk



# Download the punkt dataset required by nltk
nltk.download('punkt')

# Initialize the Google News client
gn = GoogleNews(lang='de', country='AT')

news = gn.top_news()  # gn RSS top news feed
entries = news['entries']

results = []

#append entries with title and url to results as dictionary
for entry in entries:
    results.append({"title": entry["title"], "url": entry.link})
    #print({"title": entry["title"], "url": entry.link})

articles = []

#Filter unnecessary words
filters_summary = ["freier", "zugang", "abo", "videos", "subscription", "advertisment", "advert", "add", "warentest", "ryzen"]
filters_keywords = ["das", "die", "der", "von", "dessen", "dem", "den", "des", "dass", "the", "this", "vom", "vor", "und", "oder", "bei", "für", "mit", "im", "in", "ins", "eine", "einer", "eines", "einem", "zu", "zur", "zum"]

for result in results:
    article = Article(result["url"])
    
    try:
        # Apply NLP and parse such that newspaper can generate summaries and capture keywords
        article.download()
        article.parse()
        article.nlp()

        if any(word in article.summary.lower() for word in filters_summary):
            continue
        
        keywords = [keyword for keyword in article.keywords if keyword.lower() not in filters_keywords]
        
        #truncated_summary = truncate_summary(article.summary, len_title=len(result["title"]))

        article_layout = {
            "title": result["title"],
            "url": result["url"],
            "text": article.text,
            "summary": article.summary,
            "keywords": keywords
        }
        
        articles.append(article_layout)
        #print("\n title: " + article_layout["title"] + "\n\n summary: " + article_layout["summary"] + "\n")
    except Exception as e:
        continue

def main():
    return articles