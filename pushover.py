# When pushover function is called, a string must be supplied with the desirable message.
# Also there are two optional parameters:
#    title: When supplied a string, it will be set as title of the notification, otherwise your app's name will be used
#    priority: When supplied an integer from -2 to 2, it will set the priority of the message as follows:
#        -2 generates no notification/alert
#        -1 sends as a quiet notification
#         0 (default)
#         1 displays as high-priority and bypasses the user's quiet hours
#         2 requires confirmation from the user. In that case you can manually edit the parameters 'retry' & 'expire' in the function below.

# In order for the function to work, you must set the variables 'pushover_user' and 'pushover_token' in the config.py file:
#    pushover_user is the user/group key of your user, viewable when logged into Pushover's dashboard
#    pushover_token is your application's API token

from config import pushover_user, pushover_token
import requests

def pushover(message, title='', priority=0):
    request_data = {'token':pushover_token, 'user':pushover_user, 'message':str(message), 'title':str(title), 'priority':str(priority)}
    if priority == 2:
        request_data['retry'] = '60' # how often (in seconds) the Pushover servers will send the same notification to the user (min 30 seconds)
        request_data['expire'] = '3600' # how many seconds your notification will continue to be retried for (max 10800 seconds = 3 hours)
    requests.post('https://api.pushover.net:443/1/messages.json', data = request_data)