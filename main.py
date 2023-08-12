#Libraries
import tweepy
import tracery
import requests
import os
import time
import json

from datetime import datetime, timedelta
from tracery.modifiers import base_english

#Keys
apiKey = os.getenv("apiKey")
apiSecret = os.getenv("apiSecret")

accessToken = os.getenv("accessToken")
accessTokenSecret = os.getenv("accessTokenSecret")

bearerToken = os.getenv("bearerToken")

#Data
dataUrl = "https://raw.githubusercontent.com/MythsList/twtwtbot/main/data.json"
#fileName = "data.json"

#Code
def fetchRawData(url):
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch raw data from:", url)
        return None
    
def readJsonFromFile(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except Exception as e:
        print("Failed to read JSON data from file:", e)
        return None

def generateContent(rawData):
    grammar = tracery.Grammar(rawData)
    grammar.add_modifiers(base_english)
    return grammar.flatten("#origin#")

def postContent(content):
    client = tweepy.Client(bearerToken, apiKey, apiSecret, accessToken, accessTokenSecret, wait_on_rate_limit=True)
    auth = tweepy.OAuth1UserHandler(apiKey, apiSecret, accessToken, accessTokenSecret)
    api = tweepy.API(auth)

    try:
        #client.create_tweet(text = content)
        print("Posted: ", content)
    except tweepy.TweepyException as e:
        print("Error: ", e)

def mainTask():
    rawData = fetchRawData(dataUrl)
    #rawData = readJsonFromFile(fileName)

    if rawData:
        sentence = generateContent(rawData)
        postContent(sentence)


if __name__ == "__main__":
    mainTask()