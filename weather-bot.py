import requests
import vars
import json

weatherapiURL = "https://weatherapi-com.p.rapidapi.com/current.json"
weatherapiQS = {"q": vars.coordinates}
weatherapiHeaders = {
	"content-type": "application/octet-stream",
	"X-RapidAPI-Key": vars.apikey,
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}
weatherAPIData = json.loads(requests.get(weatherapiURL, headers=weatherapiHeaders, params=weatherapiQS).text)


nameOfCity = weatherAPIData['location']['name']
nameOfState = weatherAPIData['location']['region']
currentTempF = weatherAPIData['current']['temp_f']
currentWindSpeedMPH = weatherAPIData['current']['wind_mph']
currentHumidity = weatherAPIData['current']['humidity']
currentFeelsLikeTempF = weatherAPIData['current']['feelslike_f']




print(f'The weather in {nameOfCity}, {nameOfState} is {currentTempF}. The weather feels like {currentFeelsLikeTempF}')


