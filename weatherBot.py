import requests
import keys
import json

# API Header
weatherAPIQS = {"q": keys.yourLocation, "days": "3"}
weatherAPIHeaders = {
		"content-type": "application/octet-stream",
		"X-RapidAPI-Key": keys.rapidWeatherAPIKEY,
		"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
	}
weatherAPIData = json.loads(requests.get("https://weatherapi-com.p.rapidapi.com/forecast.json", headers=weatherAPIHeaders, params=weatherAPIQS).text)

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

# Forecast (Tomorrow)
tomorrowForecastEndPoint = weatherAPIData['forecast']['forecastday'][1]['day']
tmrwMaxTempF = tomorrowForecastEndPoint['maxtemp_f']
tmrwMinTempF = tomorrowForecastEndPoint['mintemp_f']
tmrwMaxWinMPH = tomorrowForecastEndPoint['maxwind_mph']
tmrwChanceOfRain = tomorrowForecastEndPoint['daily_chance_of_rain']
tmrwTotalPrecipIN = tomorrowForecastEndPoint['totalprecip_in']
tmrwAverageHumidity = tomorrowForecastEndPoint['avghumidity']
tmrwCondition = tomorrowForecastEndPoint['condition']['text']
tmrwforecastUV = tomorrowForecastEndPoint['uv']








