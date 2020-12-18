# When telegram function is called, a string must be supplied with the desirable message.
# Also there are three optional parameters:
#    disable_notification: (boolean) When supplied with 1, it will set the message silently, users will receive notification without sound.
#    disable_web_page_preview: (boolean) When supplied with 1, it will disable link previews for links in the message.
#    parse_mode: (string) Mode for parsing entities in the message text like markdown or html.
#       You can check available parsing modes in the following url: https://core.telegram.org/bots/api#formatting-options

# In order for the function to work, you must set the variables 'telegram_token' and 'telegram_chat_id' in the config.py file:
#    telegram_token is your bot's API token. You can obtain it from BotFather. Read more: https://core.telegram.org/bots#6-botfather
#    telegram_chat_id is the unique identifier for the target chat (integer) or username of the target channel (in the format @channelusername).

from config import telegram_token, telegram_chat_id
import requests

def telegram(message, disable_notification=0, disable_web_page_preview=0, parse_mode=''):
    request_data = {'chat_id':telegram_chat_id, 'text':str(message), 'disable_notification':str(disable_notification), 'disable_web_page_preview':str(disable_web_page_preview)}
    if parse_mode:
        request_data['parse_mode'] = str(parse_mode)
    requests.post('https://api.telegram.org/bot{}/sendMessage'.format(telegram_token), data = request_data)