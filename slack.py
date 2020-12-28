# When slack function is called, a string must be supplied with the desirable message.
# In your messages you can use markdown language if needed.
#    You can find more on how to apply markdown format in your messages here: https://api.slack.com/reference/surfaces/formatting#basics
# You can also use emojis, using standard emoji code.
#    You can check supported emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/

# In order for the function to work, you must set the variable 'webhook_url' in the config.py file:
#    webhook_url is the url you should sent messages to, in order to be received by your Slack app.
#       You can find how to obtain it here: https://api.slack.com/messaging/webhooks#getting_started

from config import webhook_url
import requests
import json

def slack(message):
    request_data = {'text':str(message)}
    requests.post(webhook_url, data = json.dumps(request_data))