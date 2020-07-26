import tweepy
import os

class Bot:
    def __init__(self):
        try:
            __API_KEY = os.environ['API_KEY']
            __API_SECRET_KEY = os.environ['API_SECRET_KEY']
            __ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
            __ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']

            auth = tweepy.OAuthHandler(__API_KEY, __API_SECRET_KEY)
            auth.set_access_token(__ACCESS_TOKEN, __ACCESS_TOKEN_SECRET)
            self.api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
            self.api.verify_credentials()
            print('Authentication successful')
        except KeyError:
            print('Twitter credentials not supplied.')
        except Exception as e:
            print(e)

    def get_api(self):
        return self.api

    def recent_tweets(self):
        timeline = self.api.home_timeline()
        for tweet in timeline:
            print(f'{tweet.user.name} said {tweet.text}')
    
    def update_status(self, status):
        self.api.update_status(status)

    def get_latest_trends(self):
        # WOID for India 2282863
        trends_result = self.api.trends_place(2282863)
        for trend in trends_result[0]['trends']:
            print(trend['name'])

    def get_latest_tweets(self,id='702590808965316608'):
        allstatus = self.api.user_timeline(id=id)
        for status in allstatus:
            print(status.text)
    
    def get_all_followers(self, user=''):
        followers = self.api.followers()
        for follower in followers:
            print(f'{follower.name} id is {follower.id}')

        
