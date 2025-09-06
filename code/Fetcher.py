import feedparser
import datetime
import dotenv
import os


dotenv.load_dotenv()

CNN_RSS_FEED: str | None = os.getenv("cnn_rss_feed")
BBC_RSS_FEED: str | None = os.getenv("bbc_rss_feed")
ALJAZEERA_RSS_FEED: str | None = os.getenv("aljazeera_rss_feed")
REUTERS_RSS_FEED: str | None = os.getenv("reuters_rss_feed")

FEED_PRIORITY_QUEUE: list[str | None] = [
    BBC_RSS_FEED,
    ALJAZEERA_RSS_FEED,
    REUTERS_RSS_FEED,
    CNN_RSS_FEED
]

ranked_latest_news = []

for feed in FEED_PRIORITY_QUEUE:
    out = feedparser.parse(feed)

    if out["bozo"]:
        pass

    else:
        last_news_article_date = list(out.entries[0].published_parsed)
        last_news_article_date = datetime.datetime(*last_news_article_date[:6])
        current_time = datetime.datetime.now()
        time_difference = current_time - last_news_article_date

        hours = time_difference.total_seconds() // 3600
    
        ranked_latest_news.append({"feed": feed, "since_latest_news": int(hours)})

ranked_latest_news.sort(key=lambda e: e["since_latest_news"])
FEED = feedparser.parse(ranked_latest_news[0]["feed"])

def get_news_rss() -> tuple[str, list[dict]]:
    source: str = str(FEED.feed.title)
    news: list[dict] = []

    for entry in FEED.entries:
        try: title = entry.title
        except AttributeError: title = None
        try: summary = entry.summary
        except AttributeError: summary = None
        try: link = entry.link
        except AttributeError: link = None
        try: published = entry.published
        except AttributeError: published = None
        try: media_thumbnail = entry.media_thumbnail
        except AttributeError: media_thumbnail = None
        
        news.append({
            "title":title,
            "summary":summary,
            "link":link,
            "published":published,
            "media_thumbnail":media_thumbnail
        })

    return source, news

# FOR TESTING PURPOSES : 
# if __name__ == "__main__":
    # print(get_news_rss()[1])
    # print(get_news_rss()[0])
    # print(ranked_latest_news)
