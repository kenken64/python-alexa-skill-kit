from flask import Flask, render_template
from flask_ask import Ask, statement, question
from pymongo import MongoClient
import datetime

app = Flask(__name__)
ask = Ask(app, '/')
client = MongoClient('mongodb://pyiot:password123456@ds133166.mlab.com:33166/pyiot-stackup')
db = client['pyiot-stackup']

@ask.launch
def new_iot():
    welcome_msg = render_template('welcome')
    return question(welcome_msg)


@ask.intent('RoomTempIntent')
def roomtemp():
    temp = db.temperature
    result = ""
    temperatureValue = temp.find().sort([('modified-date', -1)]).limit(1) 
    for record in temperatureValue:
        if record['value']:
            result = record['value']
    print(">>>> " + result)
    speech_text = "Hi. This room is " + result
    return statement(speech_text).simple_card('Welcome', speech_text)    

@ask.intent('MalaysiaElection')
def malaysiaElection():
    speech_text = "Hi. Najib and Gang will WIN. Don't waste your time."
    return statement(speech_text).simple_card('Welcome', speech_text)    

@ask.intent('MalaysiaPMWife')
def malaysiaElection():
    speech_text = "Feng shui said as long his wife keep the lion king hair he will be always a winner."
    return statement(speech_text).simple_card('Welcome', speech_text)  


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)