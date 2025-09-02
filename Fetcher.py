import feedparser
import dotenv
import os


dotenv.load_dotenv()

CNN_RSS_FEED: str | None = os.getenv("cnn_rss_feeed")

FEED = feedparser.parse(CNN_RSS_FEED)

print(FEED)

