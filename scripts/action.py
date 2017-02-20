from sys import argv
import serial
import urllib.request
import requests
import json
import simplejson
import RPi.GPIO as GPIO


script, first = argv

portStatus = False
ser=serial.Serial()

if first == "on":
    GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
    GPIO.setup(7, GPIO.OUT) ## Setup GPIO Pin 7 to OUT
    GPIO.output(7,True) ## Turn on GPIO pin 7
    GPIO.setwarnings(False)
else:
    GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
    GPIO.setup(7, GPIO.OUT) ## Setup GPIO Pin 7 to OUT
    GPIO.output(7,False) ## Turn on GPIO pin 7
    GPIO.setwarnings(False)

def hpghStatus():

    url = "http://iobridge.com/api/feed/key=waStTNuoEvld6t9wsM&callback=?"

    response = urllib.request.urlopen(url)
    jsonObject = simplejson.load(response)

    lightStatus = jsonObject["module"]["channels"][0]["AnalogInput"]

    if int(float(lightStatus)) > 500:
        return True
    else:
        return False

def sendSerial(data):
    global portStatus
    global ser

    if portStatus == True:

        print 'Sending serial data...'
        print data
        try:
            ser.write(data)
        except:
            tkMessageBox.showinfo( "Atlas Laboratories", "Something went wrong. The connection was lost.")
            changeConnectStatus(False)
    else:
        tkMessageBox.showinfo( "Atlas Laboratories", "Please connect to a scanner before proceeding.")

def connect():
    global portStatus
    global ser

    if portStatus:
        ser.close()
        changeConnectStatus(False)

    else:
        try:
            port = app.serialPort.get()
            print "Attempting connection with " + port
            ser = serial.Serial(port, 9600, timeout=1)
            changeConnectStatus(True)
        except:
            print 'we fucked up'
            tkMessageBox.showinfo( "Atlas Laboratories", "Couldn't connect to the serial port. Check your connection and try again.")
            changeConnectStatus(False)
