#import packages needed
import json
import ssl
from urllib.request import urlopen, Request

def main():
    webURL = "https://api.weather.gov/points/40.1934,-85.3864"
    webContents = ssl._create_unverified_context()
    webResponse = urlopen(webURL, context=webContents)
    webData = json.load(webResponse)

    #Taking the weather url info
    weatherURL = webData["properties"]["forecast"]
    webResponse = urlopen(weatherURL, context=webContents)
    weatherData = json.load(webResponse)

    #Printing URL info
    weatherPeriods = weatherData["properties"]["periods"][:14]
    for w in weatherPeriods:
        print(w["detailedForecast"])
        print(w["temperature"])
        print("____" * 60)
        print(w["name"])




main()