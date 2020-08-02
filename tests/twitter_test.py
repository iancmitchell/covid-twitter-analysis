import unittest
import os
import sys
import json
from twitter_client import TwitterClient

class TestTwitter(unittest.TestCase):
    def setUp(self):
        print(os.environ.get('TWITTER_CREDENTIALS_FILE'))
        with open(os.environ.get('TWITTER_CREDENTIALS_FILE')) as config_file:
            config_file = config_file.read()
            config = json.loads(config_file)
            print(config)
            self.client = TwitterClient(config)

    def test_init(self):
        self.assertIsInstance(self.client, TwitterClient)

    def test_search_hashtag(self):
        self.client.search_hashtag("mask")    

if __name__ == "__main__":
    unittest.main()        