import tweepy
from . import config
from . import utils

logger = utils.get_logger()

class StreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):

        # Check if this tweet is just a mention
        if check_mentions(tweet.user.id):
            logger.info(f'Tweet is a mention and is from {tweet.user.name}')
            return

        logger.info(f'{tweet.user.id}')

        # Check if tweet is reply
        if tweet.in_reply_to_status_id is not None:
            logger.info('Tweet is a reply')
            return

        # Like and retweet if not done already
        if not tweet.favorited:
            try:
                tweet.favorite()
                logger.info(f'Tweet liked: tweet user {tweet.user.name} , tweet text {tweet.text}')
            except Exception as e:
                logger.error(f'Exception during favourite {e}')
        if not tweet.retweeted:
            try:
                tweet.retweet()
                logger.info(f'Tweet retweeted: tweet user {tweet.user.name} , tweet text {tweet.text}')
            except Exception as e:
                logger.error(f'Exception during retweet {e}')

        print(f'{tweet.user.name}:{tweet.text}')

    def on_error(self, status):
        logger.error('Error detected while running stream listener')

twitter_ids = [
    '702590808965316608',  # Abhi_indian
    '44196397',            # elonmusk
    '92708272',            # msdhoni
]

def check_mentions(user_id):
    if user_id in twitter_ids:
        return False
    return True

'''
    run_streamser starts stream listener based on keywords or selected user profiles
    params:
      mode: track/follow
      keywords: list of keywords to track for if mode is track
      twitter_ids: list of twitter id of all users to follow on
'''
def run_streamer(mode='follow', keywords=[], twitter_ids=twitter_ids):

    logger.info('Getting API')
    api_ = config.get_api()
    tweet_listener = StreamListener(api_)
    stream = tweepy.Stream(api_.auth, tweet_listener)
    
    if mode == 'follow':
        stream.filter(follow=twitter_ids, languages=['en'], is_async=False)
    elif mode == 'track':
        stream.filter(track=keywords, languages=["en"], is_async=True)
    else:
        logger.error('Please supply proper mode (follow/track)')

def test():
    logger.info('test called')
