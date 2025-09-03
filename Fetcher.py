import feedparser
import dotenv
import os


dotenv.load_dotenv()

CNN_RSS_FEED: str | None = os.getenv("cnn_rss_feeed")
BBC_RSS_FEED: str | None = os.getenv("bbc_rss_feeed")
ALJAZEERA_RSS_FEED: str | None = os.getenv("aljazeera_rss_feed")
REUTERS_RSS_FEED: str | None = os.getenv("reuters_rss_feed")

FEED = feedparser.parse(CNN_RSS_FEED)

feed_title: str = str(FEED.feed.title)
print(feed_title)

for entry in FEED.entries:
    title = entry.title
    summary = entry.summary
    link = entry.link
    published = entry.published
    media_thumbnail = entry.media_thumbnail

    print(title)
    print(summary)
    print(link)
    print(published)
    print(media_thumbnail)
