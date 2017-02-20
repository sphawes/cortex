#Scrape HackPGH for Open Status
import urllib.request
import requests
import json
import simplejson

url = "http://iobridge.com/api/feed/key=waStTNuoEvld6t9wsM&callback=?"


response = urllib.request.urlopen(url)
jsonObject = simplejson.load(response)

lightStatus = jsonObject["module"]["channels"][0]["AnalogInput"]

if int(float(lightStatus)) > 500:
    print("Open")
else:
    print("Closed")
