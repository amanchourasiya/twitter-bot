import tweepy
from . import utils
from . import config
import time

logger = utils.get_logger()
def follow_follower(api):
    logger.debug('Retreiving follower information')
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            logger.info(f'Following {follower.name}')
            follower.follow()

def follower_bot(api):
    _api = api
    while True:
        follow_follower(_api)
        logger.info('Waiting for new followers...')
        time.sleep(24 * 60 * 60)  # Sleeping for a day