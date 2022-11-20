import phonenumbers
import opencage
import folium
from phonenumbers import timezone, geocoder, carrier

print("Enter Your Number :")
no = input("")
number=("+91" + no)

print(number)

phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)
car= carrier.name_for_number(phone, "en")
reg = geocoder.description_for_number(phone, "en")

print(phone) #pepnumber
print(time)
print(car) #server_pro 
print(reg) #location

from opencage.geocoder import OpenCageGeocode

key = '07d815504f3844c994efd45e33fbc14b'
geocoder = OpenCageGeocode(key)
query = str(reg)
results = geocoder.geocode(query)

# print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)

myMap = folium.Map(location =[lat,lng] ,zoom_start =9)
folium.Marker([lat, lng], popup=reg).add_to(myMap)

myMap.save("mylocation.html")

print("Your File is Saved")
