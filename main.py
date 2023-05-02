from faceopencv import mood
from date_time import weathertime
from taggen import *
from songprofile import *
import json
import os
from helper import *
from recomender import *
from createplaylist import *

mood_tag = mood()
print('Facial Mood Detected: ', mood_tag)

weather_tag = weathertime()
print('Weather Tag: ', weather_tag)

final_tag = list(set(taggen(weather_tag, mood_tag)))
print('Final List of Tag with Priority: ', final_tag)

userSongProfile = {}
userTopSongURI = []
if os.path.exists('userSongProfile.json'):
    with open('userSongProfile.json', "r") as file:
        userSongProfile = json.load(file)
        file.close()
    with open('userTopSongURI.json', "r") as file:
        userTopSongURI = json.load(file)
        file.close()
else:
    userSongProfile, userTopSongURI = songprofile()

userMoodSongURI = []
for i in final_tag:
    userMoodSongURI += userSongProfile[i][0:5]

userSimilarSongURI = []
for i in userTopSongURI:
    songURI, artistURI = getTrackandArtistURI(i)
    similarsong = getSimilarTrack(songURI, artistURI)
    print(similarsong)
    userSimilarSongURI += similarsong
userSimilarSongURI = list(set(userSimilarSongURI))

recommendedSong = songrecommender(userMoodSongURI, userSimilarSongURI)
createplaylist(recommendedSong, mood_tag)
print('///Your Playlist has been created///')