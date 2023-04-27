import requests
import vars
import json

# API Header
weatherapiURL = "https://weatherapi-com.p.rapidapi.com/forecast.json"
weatherapiQS = {"q": vars.weatherAPICoord, "days": "3"}
weatherapiHeaders = {
	"content-type": "application/octet-stream",
	"X-RapidAPI-Key": vars.rapidWeatherAPIKEY,
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}
weatherAPIData = json.loads(requests.get(weatherapiURL, headers=weatherapiHeaders, params=weatherapiQS).text)

# WeatherAPI.com Data
# Current Weather
locationEndPoint = weatherAPIData['location']
currentEndPoint = weatherAPIData['current']
nameOfCity = locationEndPoint['name']
nameOfState = locationEndPoint['region']
currentTempF = currentEndPoint['temp_f']
currentWindSpeedMPH = currentEndPoint['wind_mph']
currentHumidity = currentEndPoint['humidity']
currentFeelsLikeTempF = currentEndPoint['feelslike_f']
currentUVIndex = currentEndPoint['uv']

# Forecast (Today)
todayForecastEndPoint = weatherAPIData['forecast']['forecastday'][0]['day']
maxTempF = todayForecastEndPoint['maxtemp_f']
minTempF = todayForecastEndPoint['mintemp_f']
maxWinMPH = todayForecastEndPoint['maxwind_mph']
chanceOfRain = todayForecastEndPoint['daily_chance_of_rain']
totalPrecipIN = todayForecastEndPoint['totalprecip_in']
averageHumidity = todayForecastEndPoint['avghumidity']
condition = todayForecastEndPoint['condition']['text']
forecastUV = todayForecastEndPoint['uv']

# Forecast (Tommorrow)
tommorrowForecastEndPoint = weatherAPIData['forecast']['forecastday'][1]['day']
tmrwMaxTempF = tommorrowForecastEndPoint['maxtemp_f']
tmrwMinTempF = tommorrowForecastEndPoint['mintemp_f']
tmrwMaxWinMPH = tommorrowForecastEndPoint['maxwind_mph']
tmrwChanceOfRain = tommorrowForecastEndPoint['daily_chance_of_rain']
tmrwTotalPrecipIN = tommorrowForecastEndPoint['totalprecip_in']
tmrwAverageHumidity = tommorrowForecastEndPoint['avghumidity']
tmrwCondition = tommorrowForecastEndPoint['condition']['text']
tmrwforecastUV = tommorrowForecastEndPoint['uv']



