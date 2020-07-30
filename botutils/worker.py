import sys
from . import config
from . import utils


class Worker:
    def __init__(self):
        self.logger = utils.get_logger()
        self.api = config.get_api()
        if self.api == None:
            self.logger.error('Failed to get api. Exiting ...')
            sys.exit(1)

    def recent_tweets(self):
        timeline = self.api.home_timeline()
        for tweet in timeline:
            self.logger.info(f'{tweet.user.name} said {tweet.text}')

    def update_status(self, status):
        self.api.update_status(status)

    def get_latest_trends(self):
        # WOID for India 2282863
        trends_result = self.api.trends_place(2282863)
        for trend in trends_result[0]['trends']:
            self.logger.info(trend['name'])

    def get_latest_tweets(self, id='702590808965316608'):
        allstatus = self.api.user_timeline(id=id)
        for status in allstatus:
            self.logger.info(status.text)

    def get_all_followers(self, user=''):
        followers = self.api.followers()
        for follower in followers:
            self.logger.info(f'{follower.name} id is {follower.id}')