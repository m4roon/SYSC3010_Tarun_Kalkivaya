from urllib2 import urlopen
from urllib import urlencode
import json
import sqlite3

# The URL that is formatted: http://api.openweathermap.org/data/2.5/weather?APPID=a808bbf30202728efca23e099a4eecc7&units=imperial&q=ottawa
# As of October 2015, you need an API key.
# I have registered under my Carleton email.
apiKey = "a808bbf30202728efca23e099a4eecc7" # If it doesnt work, get your own.

# Query the user for a city
city = raw_input("Enter the name of a city whose weather you want: ")

# Build the URL parameters
params = {"q":city, "units":"imperial", "APPID":apiKey }
arguments = urlencode(params)

# Get the weather information
address = "http://api.openweathermap.org/data/2.5/weather"
url = address + "?" + arguments

print (url)
webData = urlopen(url)
results = webData.read().decode('utf-8') # results is a JSON string
webData.close()

# Convert the json result to a dictionary
# See http://openweathermap.org/current#current_JSON for the API

data = json.loads(results)

# Print the results
windspeed = data["wind"]["speed"]
print ("Wind: %d" % windspeed)

dbconnect = sqlite3.connect("lab3.db") # Connect to database
cursor = dbconnect.cursor() # Create cursor to work with database

cursor.execute('''INSERT INTO wind VALUES(?, ?)''', (city, windspeed)) # Insert record with city and it's windspeed into table in database
dbconnect.commit() # Finalize changes
dbconnect.close() # Close connection
