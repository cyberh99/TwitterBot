import tweepy
import json

def getAPIObject(user_id):
    "Returns the api object for that user"
    with open("usuarios.json") as file: usuarios = json.load(file)
    listOfTokens = usuarios[str(user_id)]
    api = 0
    if len(listOfTokens) == 4:
        auth = tweepy.OAuthHandler(str(listOfTokens[0]), str(listOfTokens[1]))
        auth.set_access_token(str(listOfTokens[2]), str(listOfTokens[3]))
        api = tweepy.API(auth)
    
    return api