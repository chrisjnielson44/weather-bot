import tweepy
import requests
import vars
import json
import weatherBot

# RapidAPI
weatherapiURL = "https://weatherapi-com.p.rapidapi.com/current.json"
weatherapiQS = {"q": vars.weatherAPICoord}
weatherapiHeaders = {
	"content-type": "application/octet-stream",
	"X-RapidAPI-Key": vars.rapidWeatherAPIKEY,
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}
weatherAPIData = json.loads(requests.get(weatherapiURL, headers=weatherapiHeaders, params=weatherapiQS).text)

#Twitter API
Client = tweepy.Client(
    consumer_key=vars.twitterAPIKey,
    consumer_secret=vars.twitterAPIKeySecret,
    access_token=vars.twitterAccessToken,
    access_token_secret=vars.twitterAccessTokenSecret
)

weather_tweet = ''

Client.create_tweet(text=weather_tweet)




