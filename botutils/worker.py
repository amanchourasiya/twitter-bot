import tweepy
from . import api

class WorkerStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        # Like and retweet if not done already
        if not tweet.favorited:
            try:
                tweet.favorite()
            except Exception as e:
                print(f'Exception during favourite {e}')
        if not tweet.retweeted:
            try:
                tweet.retweet()
            except:
                print(f'Exception during retweet {e}')
        
        print(f'{tweet.user.name}:{tweet.text}')

    def on_error(self, status):
        print('Error detected')


def run_worker():
    api_ = api.Bot().get_api()
    tweet_listener = WorkerStreamListener(api_)
    stream = tweepy.Stream(api_.auth, tweet_listener)
    stream.filter(track=["Hacking", "Network", "Kargil"], languages=["en"], is_async=True)
    #stream.filter(follow=['445921112'])