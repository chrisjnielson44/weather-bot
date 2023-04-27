import tweepy
import requests
import vars
import json
import weatherBot

# RapidAPI
weatherapiURL = "https://weatherapi-com.p.rapidapi.com/current.json"
weatherapiQS = {"q": vars.yourLocation}
weatherapiHeaders = {
	"content-type": "application/octet-stream",
	"X-RapidAPI-Key": vars.rapidWeatherAPIKEY,
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}
weatherAPIData = json.loads(requests.get(weatherapiURL, headers=weatherapiHeaders, params=weatherapiQS).text)

#Twitter API
Client = tweepy.Client(
    consumer_key=vars.yourTwitterAPIKey,
    consumer_secret=vars.yourTwitterAPIKeySecret,
    access_token=vars.yourTwitterAccessToken,
    access_token_secret=vars.yourTwitterAccessTokenSecret
)

# Check to see if you have to wear a jacket
jacketCheckToday = ' so wear a jacket!' if weatherBot.chanceOfRain > 20 else '.'
jacketCheckTomorrow = ' so wear a jacket tomorrow!' if weatherBot.tmrwChanceOfRain > 20 else '.'

weatherTweet =  f'The current weather in {weatherBot.nameOfCity} is {weatherBot.currentTempF:.0f}\u00b0F but it feels like {weatherBot.currentFeelsLikeTempF:.0f}\u00b0F. ' \
                f'Today\'s high is {weatherBot.maxTempF:.0f}\u00b0F and today\'s low is {weatherBot.minTempF:.0f}\u00b0F. ' \
                f'The UV is {weatherBot.currentUVIndex} and there is a {weatherBot.chanceOfRain}% of rain{jacketCheckToday} ' \
                f'\n\nTomorrow\'s high is {weatherBot.tmrwMaxTempF:.0f}\u00b0F and the low is {weatherBot.minTempF:.0f}\u00b0F. ' \
                f'There is a {weatherBot.tmrwChanceOfRain}% of rain{jacketCheckTomorrow}'

Client.create_tweet(text=weatherTweet)




