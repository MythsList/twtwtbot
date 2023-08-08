#Libraries
import tweepy
import tracery
import os
import time

from tracery.modifiers import base_english

#Keys
apiKey = os.getenv("API_KEY")
apiSecret = os.getenv("API_SECRET")

accessToken = os.getenv("ACCESS_TOKEN")
accessTokenSecret = os.getenv("ACCESS_TOKEN_SECRET")

bearerToken = os.getenv("BEARER_TOKEN")

#Data
data = {
    "origin": "This is an output test: #stuff.capitalize# #stuff2# #stuff3#",
    "stuff": ["high", "low", "mid-high", "mid-low", "mid"],
    "stuff2": ["temperature", "humidity"],
    "stuff3": ["outside", "inside"]
}

#Code
def generateContent(rawData):
    grammar = tracery.Grammar(rawData)
    grammar.add_modifiers(base_english)
    return grammar.flatten("#origin#")

def postContent(content):
    client = tweepy.Client(bearerToken, apiKey, apiSecret, accessToken, accessTokenSecret, wait_on_rate_limit=True)
    auth = tweepy.OAuth1UserHandler(apiKey, apiSecret, accessToken, accessTokenSecret)
    api = tweepy.API(auth)

    try:
        #api.update_status(content)
        client.create_tweet(text = content)
        print("Posted: ", content)
    except tweepy.TweepyException as e:
        print("Error: ", e)


if __name__ == "__main__":
    sentence = generateContent(data)
    postContent(sentence)
    time.sleep(3600)