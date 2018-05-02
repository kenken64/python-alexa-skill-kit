from flask import Flask, render_template
from flask_mqtt import Mqtt
from pymongo import MongoClient
import datetime

app = Flask(__name__)
client = MongoClient('mongodb://pyiot:password123456@ds133166.mlab.com:33166/pyiot-stackup')
db = client['pyiot-stackup']

app = Flask(__name__)
app.config['MQTT_BROKER_URL'] = 'm12.cloudmqtt.com'
app.config['MQTT_BROKER_PORT'] = 13743
app.config['MQTT_USERNAME'] = 'kqcqutsu'
app.config['MQTT_PASSWORD'] = 'MP86zXZ6Zkds'
app.config['MQTT_REFRESH_TIME'] = 1.0  # refresh time in seconds
mqtt = Mqtt(app)
mqtt.subscribe('room/temp')

@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    data = dict(
        topic=message.topic,
        payload=message.payload.decode()
    )
    print(data['topic'])
    print(data['payload'])
    tempValue = {
        "value" : data['payload'],
        "modified-date" : datetime.datetime.utcnow()
    }
    temp = db.temperature
    temperValue_id = temp.insert_one(tempValue).inserted_id

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5050, debug=False)