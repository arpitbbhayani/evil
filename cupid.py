"""
Posts a love message to a group
"""
import requests
from optparse import OptionParser

# Config
FACEBOOK_ACCESS_TOKEN = None
FACEBOOK_GROUP_ID = None

# Globals
TYPES = [
    'love', 'funny', 'romantic'
]

def process(message_type):
    if FACEBOOK_GROUP_ID is None:
        print 'Please set the Facebook group ID.'
        return

    if FACEBOOK_ACCESS_TOKEN is None:
        print 'Please set the Facebook Access Token'
        return

    message_type = message_type.lower()

    if message_type.lower() == 'random':
        message_type = random.choice(TYPES)

    if message_type.lower() not in TYPES:
        print 'Unsupported message type'
        return

    # get the message

    # post the message


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-t", "--type", dest="type", default='love',
                      help="messgae type to post: love, funny, romantic, random")

    (opts, args) = parser.parse_args()

    process(opts.type)
