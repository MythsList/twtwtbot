#Libraries
import tweepy
import tracery

from tracery.modifiers import base_english

#Keys
apiKey = "API_KEY"
apiSecret = "API_SECRET"

accessToken = "ACCESS_TOKEN"
accessTokenSecret = "ACCESS_TOKEN_SECRET"

bearerToken = "BEARER_TOKEN"

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
    client = tweepy.Client(bearerToken, apiKey, apiSecret, accessToken, accessTokenSecret)
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