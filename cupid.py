"""
Posts a love message to a group
"""
import requests
from optparse import OptionParser

# Config
FACEBOOK_ACCESS_TOKEN = 'xxx'
FACEBOOK_GROUP_ID = 'xxx'

# Globals
MEDIATYPES = [
    'image'
]

GENRE = [
    'love'
]

def process(media_type, genre):
    if FACEBOOK_GROUP_ID is None:
        print 'Please set the Facebook group ID'
        return

    if FACEBOOK_ACCESS_TOKEN is None:
        print 'Please set the Facebook Access Token'
        return

    if media_type.lower() not in MEDIATYPES:
        print 'Unsupported media_type : %s' % media_type
        return

    url = 'http://speedster.pythonanywhere.com/%s/%s' % (media_type, genre)
    response = requests.get(url).json()
    if response.get('error'):
        print "Something went wrong ", response
        return

    if media_type == 'image':
        image_url = response['content']['image_url']

    message = ''

    # post the message
    response = requests.post("https://graph.facebook.com/v2.5/%s/photos" % (FACEBOOK_GROUP_ID), {
        'url': image_url,
        'message': message,
        'access_token': FACEBOOK_ACCESS_TOKEN
    }).json()

    print response



if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-t", "--type", dest="type", default='image',
                      help="messgae type to post: image")
    parser.add_option("-g", "--genre", dest="genre", default='love',
                      help="messgae genre to post: love")

    (opts, args) = parser.parse_args()

    process(opts.type, opts.genre)
