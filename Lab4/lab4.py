# USING Python v3.8.3

from urllib.parse import urlencode
from http.client import HTTPConnection

key = 'AT68QYQ94MQEWXL3'

if __name__ == "__main__":

    group = 'L3-T-4'
    email = 'tarunkalikivaya@cmail.carleton.ca'
    identifier = 'b'
    
    params = urlencode({'field1': group, 'field2': email, 'field3': identifier, 'key':key }) # Parsing field1, field2, field3, and key into url
    headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"} # Additional info for request
    conn = HTTPConnection("api.thingspeak.com:80") # Setting connection to Thingspeak server to perform request
        
    try:
        conn.request("POST", "/update", params, headers) # Sending write request here

        response = conn.getresponse() # Getting response of request
        print (response.status, response.reason)

        #data = response.read()

        conn.close()
    except:
        print("Write Failed")
