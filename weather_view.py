import time

def StartView(): 
	print("\n\n---Welcome to Weather Forecast Engine---")
	print("[N] for New Search")
	print("[Q] for Quit")
	return "Enter your Choice :" 
	

def EndView():
	print("\nThank you for using the Weather Forecast Engine.\nHave a great day! :)")
	return

def InvalidEntry():
	print("\n>>>>ERROR<<<< : Invalid Entry!\n")

def LocationView():
	return "\nEnter Location :"

def LocationSuccess(sList):
	time.sleep(2)
	print("\nLocation identified :",sList[0], sList[1],'\n')
	time.sleep(2)
	return

def LocationFailed(location):
	print("\n\n>>>>ERROR<<<< : ", location, "not in database.\n\n")
	return

def ViewWeather(city, country, weather_dict):
	print("Weather Forecast Details for", city, country,'\n')
	time.sleep(2)
	# print(weather_dict)
	for i in weather_dict:
		print('date:', weather_dict[i][0])
		print('temperature:', weather_dict[i][1])
		print('humidity:', weather_dict[i][2])
		print('wind speed:', weather_dict[i][3])
		# print('min_temp:',weather_dict[i][4])
		# print('max_temp:',weather_dict[i][5],'\n\n')
		time.sleep(4)
	return



	