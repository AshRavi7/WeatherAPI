import weather_view # importing functions from model.py 
import weather_model # importing functions from view.py 
import logging  # logs every debugging step in the log file "weather_app.log"

def GetChoice():
	'''Get choice from user:
		N/n - New Search
		Q/q - Quit			'''  
	choice=input(weather_view.StartView())
	logging.info("inside GetChoice()")
	# 1. weather_view.StartView()
	if choice.lower() =='q':
		# 2. weather_view.EndView()
		logging.info("Quitting the Application")
		weather_view.EndView()
	elif choice.lower()=='n':
		# 3. GetLocation() 
		logging.info("New Search Option selected.")
		search=GetLocation()
	else:
		logging.warning("Invalid Entry.")
		weather_view.InvalidEntry()
		# 4. weather_view.InvalidEntry()
		GetChoice()

def GetLocation():
	location=input(weather_view.LocationView()) # mumbai 
	# 5. weather_view.LocationView()
	search=weather_model.LocationSearch(location.capitalize()) # search is holding a list of values
	# 6. weather_model.LocationSearch(location)
	if search[0]=='Success':
		weather_view.LocationSuccess([search[1], search[2]])
		# 7. weather_view.LocationSuccess()
		weather_dict = weather_model.WeatherDetails(search[1], search[2], search[3])
		# 8. weather_model.WeatherDetails()
		weather_view.ViewWeather(search[1], search[2], weather_dict)
		GetChoice()
	else:
		weather_view.LocationFailed(location)
		GetChoice()


if __name__== '__main__': # main method 
	logging.basicConfig(filename='weather_app.log', filemode='a', format='%(asctime)s>>>%(process)d---%(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
	GetChoice() # function call 