import twitter
import os 
from typing import List
import json

class TwitterClient(object):
    def __init__(self, config_path: str = os.environ.get('TWITTER_CREDENTIALS_FILE')):
        self.client = self._init_client(config_path) 

    def _init_client(self, config_path: str) -> twitter.Api:
        with open(os.environ.get('TWITTER_CREDENTIALS_FILE')) as config_file:
            config_file = config_file.read()
            config = json.loads(config_file)
        return twitter.Api(consumer_key=config.get('apiKey'), consumer_secret=config.get('apiSecret'), access_token_key=config.get('accessToken'), access_token_secret=config.get('accessTokenSecret'))

    def search_hashtag(self, hashtag: str) -> List:
        tweet_data = self.client.GetSearch(raw_query=f"q=%23{hashtag}")
        print(type(tweet_data[0]))
        data = []
        columns = ["id","location","created_at","text"]
        for status in tweet_data:
            row = {}
            print("Status: ",status)
            for column in columns:
                row[column] = getattr(status, column)
            data.append(row)    
        return data