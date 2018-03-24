# Dependencies
import tweepy
import json
#from config import ConsumerKey, ConsumerSecret, AccessToken, AccessTokenSecret
from random import choice
import time
import os

# Twitter API Keys
consumer_key = os.environ['ConsumerKey']
consumer_secret = os.environ['ConsumerSecret']
access_token = os.environ['AccessToken']
access_token_secret = os.environ['AccessTokenSecret']

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

happy_quotes = [
    "For every minute you are angry you lose sixty seconds of happiness. - Ralph Waldo Emerson",
    "Folks are usually about as happy as they make their minds up to be. - Abraham Lincoln",
    "Happiness is when what you think, what you say, and what you do are in harmony. - Mahatma Gandhi",
    "Count your age by friends, not years. Count your life by smiles, not tears. - John Lennon",
    "Happiness is a warm puppy. - Charles M. Schulz",
    "The happiness of your life depends upon the quality of your thoughts. - Marcus Aurelius",
    "Now and then it's good to pause in our pursuit of happiness and just be happy. - Guillaume Apollinaire"]
i = 0
while i < 7:
<<<<<<< HEAD
<<<<<<< HEAD
    try:
        api.update_status(choice(happy_quotes)+str(i))
        print("tweet successfully!")
        i += 1
        time.sleep(10)
    except:
        pass
=======
=======
>>>>>>> 0a547150092b8f6be3998d6e83239c7bf21bc9da
    api.update_status(choice(happy_quotes))
    print("tweet successfully!")
    i += 1
    time.sleep(10)
<<<<<<< HEAD
>>>>>>> 0a547150092b8f6be3998d6e83239c7bf21bc9da
=======
>>>>>>> 0a547150092b8f6be3998d6e83239c7bf21bc9da
