import feedparser
import dotenv
import os


dotenv.load_dotenv()

CNN_RSS_FEED: str | None = os.getenv("cnn_rss_feeed")
BBC_RSS_FEED: str | None = os.getenv("bbc_rss_feeed")
ALJAZEERA_RSS_FEED: str | None = os.getenv("aljazeera_rss_feed")
REUTERS_RSS_FEED: str | None = os.getenv("reuters_rss_feed")
# TODO: SWITCH SOURCES IF THE CURRENT ONE IS DOWN / HASN'T BEEN UPDATED
FEED = feedparser.parse(CNN_RSS_FEED)

def get_news_rss() -> tuple[str, list]:
    source: str = str(FEED.feed.title)
    
    news: list = []

    for entry in FEED.entries:
        title = entry.title
        summary = entry.summary
        link = entry.link
        published = entry.published
        media_thumbnail = entry.media_thumbnail
        
        news.append({
            "title":title,
            "summary":summary,
            "link":link,
            "published":published,
            "media_thumbnail":media_thumbnail[0]
        })

    return source, news


if __name__ == "__main__":
    print(get_news_rss())
