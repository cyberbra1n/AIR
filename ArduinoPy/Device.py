import serial
import time
from sys import platform as _platform
import subprocess

#TODO: make and import settings file for specific arduino board
#      look in getStatus (14 is hardcoded)

class Device(object):

    #Device class is an abstract class for arduino device.
    #It provides some essential functions to connect and easy
    #communicate with arduino code(which is provided on <URL>)

    def __init__(self):
        super(Device, self).__init__() # basic object class
        self.PIPE = subprocess.PIPE
        self.device = None

    def findDevice(self, os):
        #finds Arduino devices on mashine and returns list of devices
        #list possible devices 
        if os == "linux" or os == "linux2" or "Linux":
            ls = subprocess.Popen(["ls /dev/ttyACM*"], stdout = self.PIPE, shell=True)
            ls = ls.communicate()[0] # returns raw ls output
            #parse and return list of devices
            ls = ls.rstrip()
            ls = ls.split("\n")
            return ls

        elif os == "win32":
        #TODO:implement for windows
            pass
        elif os == "darwin":
        #TODO:implement for iOS
            pass
        else:
            print "Unknown OS. Check documentation."

    def getDevice(self, devicePath):
    #returns serial connection object with device 
    #provided by devicePath
        if(serial.Serial(devicePath, 9600)):
            self.device = serial.Serial(devicePath, 9600); #local pickup for internal use of library
            return self.device #return pickup for external use
        else:
            self.device = None #local pickup
            return None #return pickup

    def getDigitalStatus(self, device):
    #function returns array of all digital
    #ports to status variable.
    #if element is True pin is HIGH.
    #if element is False pin is LOW.
        device.write("0")
        device.flushInput()
        response = []
        for each in range(0,14): #this is 14 from TODO comment
            try:
                arduinoRead = device.readline().strip("\r\n")
                if arduinoRead == '0':
                    response.append(False)
                elif arduinoRead == '1':
                    response.append(True)
                else:
                    exit("Received value different then 0 or 1 in Device.getStatus()")
            except:
                print "No response to signal 0"
        return response

    def getStatusForDigitalByPorts(self, device, ports):
    #ports array of ints in domain 0-13
    #get status only for selected ports
    #parsing return value from getDigitalStatus
      status = self.getDigitalStatus(device)
      #print status
      reqPortsStatus = []
      for required in ports:
        exit(required)
        reqPortsStatus.append(status[required])
      return reqPortsStatus
    
    def writeCharViaSerial(self, device, char):
        #writes character via serial port
        #arduino should have listener functions for char that is sent
        #TODO:generic make arduino code
        device.write(char)
        try:
            device.flushOutput()
        except:
            print "No response to char", char

    def writeStringViaSerial(self, device, string):
        #TODO:make function for passing message not only char (+ arduino 'listen/getString' logic)
        #TODO:generic make arduino code
        pass

    #def monitorAnalogPort(self, device, port):
    #    while True:
    #        value = device.readline()
      
    def readSerialOnce(self, device):
        val = device.readline()
        device.flushInput()
        device.flushOutput()
        return val
        
