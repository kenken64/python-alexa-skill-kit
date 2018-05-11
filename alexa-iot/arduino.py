import serial
import paho.mqtt.client as paho

broker="m12.cloudmqtt.com"
port=13743

def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass

mqttClient= paho.Client("tempControl")                           #create client object
mqttClient.on_publish = on_publish                      #assign function to callback
mqttClient.username_pw_set('kqcqutsu', 'MP86zXZ6Zkds')
mqttClient.connect(broker,port, 60)                                 #establish connection

ser = serial.Serial(
    port='/dev/ttyACM0',\
    baudrate=9600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0)

print("connected to: " + ser.portstr)
count=1
s = ""

while True:
    for line in ser.readline():
        print(str(count) + str(': ') + chr(line) )
        count = count+1
        if chr(line) != '@':
            s += chr(line)
        if(chr(line) == '@'):
            if(s != ''):
                ret= mqttClient.publish("room/temp",s)     
                print(ret)
            print(s)
            s = ""

ser.close()