from geopy.geocoders import Nominatim 


geolocator = Nominatim(user_agent="geoapiExercises") 

Latitude = "19.1627264"
Longitude = "72.99072"

location = geolocator.reverse(Latitude+","+Longitude) 
address = location.raw['address'] 
print(location.raw)
display_name = address.get('display_name')
city = address.get('city') 
state = address.get('state_district') 
country = address.get('country', '') 
code = address.get('country_code') 
zipcode = address.get('postcode') 

print('Display Name : ',address.keys())
print('City : ', city) 
print('State : ', state) 
print('Country : ', country) 
print('Zip Code : ', zipcode)
