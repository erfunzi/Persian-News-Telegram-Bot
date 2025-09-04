import feedparser
import dotenv
import os


dotenv.load_dotenv()

CNN_RSS_FEED: str | None = os.getenv("cnn_rss_feed")
BBC_RSS_FEED: str | None = os.getenv("bbc_rss_feed")
ALJAZEERA_RSS_FEED: str | None = os.getenv("aljazeera_rss_feed")
REUTERS_RSS_FEED: str | None = os.getenv("reuters_rss_feed")

FEED_PRIORITY_QUEUE: list[str | None] = [
    CNN_RSS_FEED,
    BBC_RSS_FEED,
    ALJAZEERA_RSS_FEED,
    REUTERS_RSS_FEED
]

# TODO: SWITCH SOURCES IF THE CURRENT ONE IS DOWN ( the "bozo" field would flip to 1 )/ HASN'T BEEN UPDATED
# TODO: FIX SOME ISSUES WITH GETTING THE INFO FROM OTHER SOURCES ( more flexibility probably )

for feed in FEED_PRIORITY_QUEUE:
    out = feedparser.parse(feed)
    
    if out["bozo"] == False:
        FEED = out
        break

    if out["bozo"]:
        pass

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
    print(get_news_rss()[0])
