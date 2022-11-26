import time
import os
import datetime
import random
import wiotp.sdk.application
#CallBack function to receive the commands from cloud
def myCommandCallback(cmd):
 print ("Message received from IBM IoT Platform: %s" )
 cmd.data(['command'])
 m = cmd.data['command']
 if(m=="motoron"):
  print("Motor is switched on")
 elif(m=="motoroff"):
  print("Motor is switched OFF")
print(" ")
#Device credentials
myConfig = {
"identity": {
"orgId": "1v150i",
"typeId": "weather_device",
"deviceId": "weather_today"
},
"auth": {
"token": "J2qEAJhe2npnh-Nj1D"
}
}
#Making Connection to cloud
client = wiotp.sdk.device.DeviceClient(config=myConfig,
logHandlers=None)
client.connect()
#Sending data for every 5000 seconds to cloud
while True:
 soil=random.randint(0, 100)
 temp=random.randint(0,125)
 hum=random.randint(0, 100)
 myData={'soil_moisture': soil, 'temperature': temp, 'humidity':hum}
 client.publishEvent(eventId="status", msgFormat="json",
 data=myData, qos=0, onPublish = None)
 print("Published data Successfully: %s", myData)
 time.sleep(5000)
 client.commandCallback = myCommandCallback
#Disconnected from cloud
client.disconnect()
