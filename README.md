# Twitter Bot
A bot based on Twitter API which will auto respond to tweets from specific accounts and regularly post updates.

## Getting Started
To run this all you can run locally or in a docker container

### Prerequisites
The only prequisite is the API keys and ACCESS tokens for twitter developer API.
[Twitter developer API](https://developer.twitter.com/en)

For running locally
```
python3 bot.py
```

For running in docker container
Latest docker image of this repository is built regularly at aes256/twitter-bot:latest
```
docker run -ti --name twitter-bot aes256/twitter-bot
```

