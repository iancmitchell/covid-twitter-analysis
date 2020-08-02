import twitter
import os 


class TwitterClient(object):
    def __init__(self, config: dict):
        self.client = self._init_client(config) 

    def _init_client(self, config) -> twitter.Api:
        return twitter.Api(consumer_key=config.get('apiKey'), consumer_secret=config.get('apiSecret'), access_token_key=config.get('accessToken'), access_token_secret=config.get('accessTokenSecret'))

    def search_hashtag(self, hashtag: str):
        tweet_data = self.client.GetSearch(raw_query=f"q=%23{hashtag}")
        print(tweet_data)