import os,sys
import urllib.request
import json

#Important information about JSON
#http://docs.python-guide.org/en/latest/scenarios/json/
# extra=['.','[',']','(',')','m720p','480p','480','DVDSCR','BrRip','New Source','MP3','Mafiaking','1CD',
# 'mkv','mSD','2CD','BRRip','BRrip','720p','BluRay','YIFY','mp4','XviD','-','x264','ETRG','avi','StyLishSaLH'
# ,'DVD','dvd','DVDRip','RIP','rip','Rip','Back In Action']

path = "A:\\Movies"
listOfDir = os.listdir(path)
for file in listOfDir:
    # for k in extra:
    #     if(k in file):
    #         file = file.replace(k," ")
    filePlus = file.replace(" ","+")
    str ='?t='+filePlus
    url = "http://www.omdbapi.com/"+str+"&y=&plot=short&r=json"
    bytesResponse = urllib.request.urlopen(url).read()
    strResponse = bytesResponse.decode('utf-8')
    values = json.loads(strResponse)
    if(values['Response']=="False"):
        print("Movie not found! ("+file+")")
    else:
        print(values['Title']+" "+values['imdbRating'])
        tempRate = values['imdbRating']
        os.rename(os.path.join(path, file),os.path.join(path,file+" "+tempRate))

