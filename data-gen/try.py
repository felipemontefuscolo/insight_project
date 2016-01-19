import tweepy
import urllib2
import json
consumer_key='#'
consumer_secret='#'
access_token_key='#'
access_token_secret='#'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
api = tweepy.API(auth)

public_tweets = api.user_timeline(screen_name="@Felipe",include_rts=True)
all_items=[]
[all_items.append(i) for i in public_tweets]

for i in all_items:
    try:
        if i.retweeted_status:
            print i.retweeted_status.text
    except:
        pass
