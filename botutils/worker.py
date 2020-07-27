import tweepy
from . import api


class WorkerStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):

        # Check if this tweet is just a mention
        if check_mentions(tweet.user.id):
            print(f'Tweet is a mention and is from {tweet.user.name}')
            return

        print(f'{tweet.user.id}')

        # Check if tweet is reply
        if tweet.in_reply_to_status_id is not None:
            return

        # Like and retweet if not done already
        if not tweet.favorited:
            try:
                tweet.favorite()
            except Exception as e:
                print(f'Exception during favourite {e}')
        if not tweet.retweeted:
            try:
                tweet.retweet()
            except Exception as e:
                print(f'Exception during retweet {e}')

        print(f'{tweet.user.name}:{tweet.text}')

    def on_error(self, status):
        print('Error detected')


twitter_ids = [
    '702590808965316608',  # Abhi_indian
    '44196397',            # elonmusk
    '92708272',            # msdhoni
]


def run_worker():
    api_ = api.Bot().get_api()
    tweet_listener = WorkerStreamListener(api_)
    stream = tweepy.Stream(api_.auth, tweet_listener)
    #stream.filter(track=["Hacking"], languages=["en"], is_async=True)
    stream.filter(follow=twitter_ids)

def check_mentions(user_id):
    if user_id in twitter_ids:
        return False
    return True