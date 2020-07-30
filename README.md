# Twitter Bot
A bot based on Twitter API which will auto respond to tweets from specific accounts and regularly post updates.

## Getting Started
To run this all you can run locally or in a docker container

### Prerequisites
The only prequisite is the API keys and ACCESS tokens for twitter developer API.
[Twitter developer API](https://developer.twitter.com/en)

## Deployment
For running locally
```
python3 bot.py
```

For running in docker container
Latest docker image of this repository is built regularly at aes256/twitter-bot:latest
```
docker run -ti 
      -e ACCESS_TOKEN="<access token>"
      -e ACCESS_TOKEN_SECRET="access token secret"
      -e API_KEY="api key"
      -e API_SECRET_KEY="api secret key"
      --name twitter-bot aes256/twitter-bot
```
These environment variables should be set from the values from twitter developer API.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* [Tweepy python library for twitter](https://www.tweepy.org)
