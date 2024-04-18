import os
from dotenv import load_dotenv
from robot import Bot


# load environment variables
load_dotenv()
phrase = os.getenv('phrase')
topic = os.getenv('topic')
website = os.getenv('website')


# instantiate a Bot
bot = Bot(website, phrase, topic)

# transverse yahoo news website and scrape news
bot.transverse()
