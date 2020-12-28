# Pushover function call example:
from pushover import pushover
pushover('Test message', 'Test title', 1) # Last two parameters are optional.


# Telegram function call example:
from telegram import telegram
telegram('Test message', 1, 1, 'markdownv2') # Last three parameters are optional.


# Slack function call example:
from slack import slack
slack('Test message')