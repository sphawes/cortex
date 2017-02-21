from sys import argv
#import urllib.request
import requests
import json as simplejson
import RPi.GPIO as GPIO

script, first = argv

def turnLedOn():
    GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
    GPIO.setwarnings(False)
    GPIO.setup(40, GPIO.OUT) ## Setup GPIO Pin 40 to OUT
    GPIO.output(40,True) ## Turn on GPIO pin 40



def turnLedOff():
    GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
    GPIO.setwarnings(False)
    GPIO.setup(40, GPIO.OUT) ## Setup GPIO Pin 40 to OUT
    GPIO.output(40,False) ## Turn on GPIO pin 40


#def hpghStatus():

#    url = "http://iobridge.com/api/feed/key=waStTNuoEvld6t9wsM&callback=?"

#    response = urllib.request.urlopen(url)
#    jsonObject = simplejson.load(response)

#    lightStatus = jsonObject["module"]["channels"][0]["AnalogInput"]

#    if int(float(lightStatus)) > 500:
#        return True
#    else:
#        return False


if first == "on":
    turnLedOn()
else:
    turnLedOff()
