import json
import requests
import datetime
import logging 

def LocationSearch(location): 
	'''Check whether we have data for the location entered.
	>> load city_list.json
	>> if location entered by user is present in city_list.json, success
	>> else failed'''
	with open("city_list.json","r", encoding="utf8") as cityJSON:
		data=json.load(cityJSON)	# see city_list.json

	for item in data:
		if item['name']==location:
			logging.info(f"{location} present in the city_list.json")
			return ['Success', item['name'], item['country'], item['id']]
	logging.error(f"{location} not present in the city_list.json")
	return ['Failed', location]

def WeatherDetails(city, country, id):
	url='http://api.openweathermap.org/data/2.5/forecast?id='+str(id)+'&APPID=1960401d79b51d8c3be286b9463a081b'
	response=requests.get(url)
	weather_details=json.loads(response.text)
	weather_dict = dict()
	for i in range(4):
		dt_txt = weather_details['list'][i]['dt_txt']
		temp = round(int(weather_details['list'][i]['main']['temp'])-273.15, 2)
		min_temp = round(int(weather_details['list'][i]['main']['temp_min'])-273.15, 2)
		max_temp = round(int(weather_details['list'][i]['main']['temp_max'])-273.15, 2)
		humidity = weather_details['list'][i]['main']['humidity']
		wind_speed = weather_details['list'][i]['wind']['speed']
		weather_dict[i]=[dt_txt, temp, humidity, wind_speed]
	return weather_dict