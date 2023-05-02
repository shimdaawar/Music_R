from datetime import datetime
import geocoder
from pyowm import OWM

now = datetime.now()

current_time = int(now.strftime("%H"))
print("Current Time =", current_time)

time_slot = ""

if 4 <= current_time <= 11:
    time_slot = "M"
elif 11 < current_time <= 16:
    time_slot = "A"
elif 16 < current_time <= 19:
    time_slot = "E"
elif (0 <= current_time < 4) or current_time > 19:
    time_slot = "N"

g = geocoder.ip('me')
lat, lng = g.latlng

owm = OWM('8aa4f173bbbb157abbce710e59499f7c')  # Replace YOUR_API_KEY with your OpenWeatherMap API key
mgr = owm.weather_manager()
observation = mgr.weather_at_coords(lat, lng)
weather = observation.weather

print(f"Current weather: {weather.detailed_status}")
w = weather.detailed_status

w_final = ""

if w == "clear sky":
    w_final = "CS"
elif w == "few clouds" or w == "scattered clouds" or w == "broken clouds" or w == "overcast clouds":
    w_final = "C"
elif w == "shower rain" or w == "rain" or w == "thunderstorm":
    w_final = "R"
elif w == "snow":
    w_final = "S"
else:
    w_final = "M"

tags = []
if w_final == "CS":
    tags = ["Happy", "Neutral", "Angry"]
elif w_final == "C":
    tags = ["Sad", "Happy", "Neutral"]
elif w_final == "R":
    tags = ["Sad", "Fear", "Neutral"]
elif w_final == "S":
    tags = ["Happy", "Fear", "Neutral"]
elif w_final == "M":
    tags = ["Fear", "Neutral", "Sad"]


def weathertime():
    return tags


def timeslot():
    return time_slot
