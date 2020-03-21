from slacker import Slacker
def send(message):
    slack=Slacker('')
    slack.chat.post_message('#general',message)