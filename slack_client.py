from slacker import Slacker
def send(message):
    slack=Slacker('xoxb-1002164459762-1003706611971-iepYghXcYVR1gvWwnpAQadba')
    slack.chat.post_message('#general',message)