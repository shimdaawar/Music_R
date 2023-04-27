from faceopencv import mood
from date_time import weathertime
from taggen import *
from songprofile import *
import subprocess
import json
from helper import *
from recomender import *
from createplaylist import *

mood_tag=mood()

weather_tag=weathertime()
print(weather_tag)

final_tag= list(set(taggen(weather_tag,mood_tag)))

userSongProfile,userTopSongURI= songprofile()

userMoodSongURI=[]
for i in  final_tag:
    userMoodSongURI+=userSongProfile[i][0:5]
    
userSimilarSongURI=[]
for i in userTopSongURI:
    songURI,artistURI = getTrackandArtistURI(i)
    print(songURI,artistURI)
    similarsong= getSimilarTrack(songURI,artistURI)
    print(similarsong)
    userSimilarSongURI+=similarsong
userSimilarSongURI=list(set(userSimilarSongURI))

recommendedSong=songrecommender(userMoodSongURI, userSimilarSongURI)

createplaylist(recommendedSong,mood_tag)
