import serial
from sys import argv

script, first = argv

portStatus = False
ser=serial.Serial()

def changeConnectStatus(state):
    global portStatus

    if state:
        portStatus = True
        app.connectButton.configure(text = "Connected!")
        print "Port Status: " + str(portStatus)

    else:
        portStatus = False
        app.connectButton.configure(text = "Connect")
        print "Port Status: " + str(portStatus)

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
