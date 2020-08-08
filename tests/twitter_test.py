import unittest
import os
import sys
import json
from twitter_client import TwitterClient

class TestTwitter(unittest.TestCase):
    def setUp(self):        
        self.client = TwitterClient()

    def test_init(self):
        self.assertIsInstance(self.client, TwitterClient)

    def test_search_hashtag(self):
        self.client.search_hashtag("mask")    

if __name__ == "__main__":
    unittest.main()        