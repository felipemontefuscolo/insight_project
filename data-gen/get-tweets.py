#!/usr/bin/env python

# Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from datetime import datetime
from pprint import pprint
import json
import os

# loads Twitter credentials from .twitter file that is in the same directory as this script
file_dir = os.path.dirname(os.path.realpath(__file__)) 
with open(file_dir + '/credentials.twitter') as twitter_file:  
    twitter_cred = json.load(twitter_file)

# authentication from the credentials file above
access_token = twitter_cred["access_token"]
access_token_secret = twitter_cred["access_token_secret"]
consumer_key = twitter_cred["consumer_key"]
consumer_secret = twitter_cred["consumer_secret"]

class StdOutListener(StreamListener):
    """ A listener handles tweets that are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def __init__(self, filename):
        self.filename = filename

    # this is the event handler for new data
    def on_data(self, data):
        if not os.path.isfile(self.filename):    # check if file doesn't exist
            f = file(self.filename, 'w')
            f.close()
        with open(self.filename, 'ab') as f:
            #print "writing to {}".format(self.filename)
            #f.write(data)
            0+0
        f.closed
#        return True
        jsonData=json.loads(data)
        text=jsonData['text']
        text2=jsonData['entities']['hashtags']
        for hashtag in text2:
             text2=hashtag['text']
        #print text+str(text2)
        retweeted_status = "///////////////////"
        try:
            retweeted_status=jsonData['retweeted_status']
            #print retweeted_status
            #print jsonData['text']
            print jsonData
        except:
            pass
            #print jsonData
            #f.write(data)
        return True
        
    # this is the event handler for errors    
    def on_error(self, status):
        print(status)

    def on_status(self, status):
        if not hasattr (status, 'retweeted_status'): 
            print "ai"
        else:
            print status.text
               

if __name__ == '__main__':
    listener = StdOutListener(file_dir + "/tweets.txt")
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # NOTE: The streaming API doesn't allow to filter by location AND keyword simultaneously.
    print "Use CTRL + C to exit at any time.\n"
    stream = Stream(auth, listener)
    #stream.filter(track=['#felipe'], locations=[-180,-90,180,90]) # this is the entire world, any tweet with geo-location enabled
    stream.filter(track=['obama']) 
    #stream.filter(locations=[-180,-90,180,90]) 
