from twilio.rest import Client
import requests
import vars
import json
import weatherBot

# WeatherAPI.com
weatherapiURL = "https://weatherapi-com.p.rapidapi.com/current.json"
weatherapiQS = {"q": vars.yourLocation}
weatherapiHeaders = {
	"content-type": "application/octet-stream",
	"X-RapidAPI-Key": vars.rapidWeatherAPIKEY,
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}
weatherAPIData = json.loads(requests.get(weatherapiURL, headers=weatherapiHeaders, params=weatherapiQS).text)

# Twilio API
account_sid = vars.twilioSID
auth_token = vars.twilioAuthToken
client = Client(account_sid, auth_token)

if weatherBot.chanceOfRain > 20:
    coatcheckToday = ' so wear a jacket!'
elif weatherBot.tmrwChanceOfRain > 20:
    coatcheckTmrw = ' so wear a jacket tomorrow!'
else:
    coatcheckToday, coatcheckTmrw = ''

weatherMessage = f'The current weather is {weatherBot.currentTempF:.0f}\u00b0F but it feels like {weatherBot.currentFeelsLikeTempF}\u00b0F. ' \
                f'\nToday\'s high is {weatherBot.maxTempF:.0f}\u00b0F and today\'s low is {weatherBot.minTempF:.0f}\u00b0F.' \
                f'The UV is {weatherBot.currentUVIndex} and there is a {weatherBot.chanceOfRain}\% of rain{coatcheckToday}' \
                f'\nTomorrow\'s high is {weatherBot.tmrwMaxTempF}\u00b0F and the low is {weatherBot.minTempF}\u00b0F' \
                f'There is a {weatherBot.tmrwChanceOfRain}% of rain{coatcheckTmrw}'

message = client.messages \
				.create(
                     body=weatherMessage,
                     from_=vars.twilioFrom,
                     to=vars.twilioTo
                 )
