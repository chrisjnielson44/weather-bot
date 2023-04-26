import tweepy
import requests
import vars
import json

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

# WeatherAPI.com Data
locationEndPoint = weatherAPIData['location']
currentEndPoint = weatherAPIData['current']

nameOfCity = locationEndPoint['name']
nameOfState = locationEndPoint['region']
currentTempF = currentEndPoint['temp_f']
currentWindSpeedMPH = currentEndPoint['wind_mph']
currentHumidity = currentEndPoint['humidity']
currentFeelsLikeTempF = currentEndPoint['feelslike_f']


tweet = f'The weather in {nameOfCity}, {nameOfState} is {currentTempF}. The weather feels like {currentFeelsLikeTempF}'


Client.create_tweet(text=tweet)




