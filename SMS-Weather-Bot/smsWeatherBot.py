from twilio.rest import Client
import requests
import keys
import json
import weatherBot

# WeatherAPI.com
weatherapiURL = "https://weatherapi-com.p.rapidapi.com/current.json"
weatherapiQS = {"q": keys.yourLocation}
weatherapiHeaders = {
	"content-type": "application/octet-stream",
	"X-RapidAPI-Key": keys.rapidWeatherAPIKEY,
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}
weatherAPIData = json.loads(requests.get(weatherapiURL, headers=weatherapiHeaders, params=weatherapiQS).text)

# Twilio API
account_sid = keys.twilioSID
auth_token = keys.twilioAuthToken
client = Client(account_sid, auth_token)

coatcheckToday = '- so wear a jacket!' if weatherBot.chanceOfRain > 20 else '.'
coatcheckTmrw = '-so wear a jacket tomorrow!' if weatherBot.tmrwChanceOfRain > 20 else '.'

weatherMessage = f'\nCurrent temp: {weatherBot.currentTempF:.0f}\u00b0F but it feels like {weatherBot.currentFeelsLikeTempF:.0f}\u00b0F' \
                f'\nToday\'s high: {weatherBot.maxTempF:.0f}\u00b0F' \
                f'\nToday\'s low: {weatherBot.minTempF:.0f}\u00b0F' \
                f'\nToday\'s chance of rain: {weatherBot.chanceOfRain}% {coatcheckToday}' \
                f'\n\nTomorrow\'s High: {weatherBot.tmrwMaxTempF:.0f}\u00b0F' \
                f'\nTomorrow\'s Low: {weatherBot.tmrwMinTempF:.0f}\u00b0F' \
                f'\nChance of rain tomorrow: {weatherBot.tmrwChanceOfRain}% {coatcheckTmrw} '\

message = client.messages \
				.create(
                     body=weatherMessage,
                     from_=keys.twilioFrom,
                     to=keys.twilioTo
                 )
