from robot import Bot
from robocorp.workitems import inputs


# Load the next input work item from the queue
item = inputs.current

# Access work item variables
phrase = item.payload.get('phrase')
topic = item.payload.get('topic')
website = item.payload.get('website')

# instantiate a Bot
bot = Bot(website, phrase, topic)

# transverse yahoo news website and scrape news
bot.transverse()
