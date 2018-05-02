<a href="https://www.youtube.com/watch?v=vXw9tzfwlvw" target="_blank"><img src="https://i.ytimg.com/vi/vXw9tzfwlvw/1.jpg" 
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>

# Python Dependencies
```
pip install flask
pip install flask_ask
pip install pymongo
pip install paho-mqtt
```
# Running all the program
```
python alexa-iot/arduino.py
python alexa-iot/server.py
python alexa-iot/device-broker.py
```


# Alexa Skills JSON Configuration
```
{
    "interactionModel": {
        "languageModel": {
            "invocationName": "iot stackup",
            "intents": [
                {
                    "name": "AMAZON.CancelIntent",
                    "samples": []
                },
                {
                    "name": "AMAZON.HelpIntent",
                    "samples": []
                },
                {
                    "name": "AMAZON.StopIntent",
                    "samples": []
                },
                {
                    "name": "RoomTempIntent",
                    "slots": [],
                    "samples": [
                        "room temperature",
                        "what is the temperature of this room",
                        "I feel cold do i need to wear extra jacket",
                        "Is hot here",
                        "Hey what is the room temperature"
                    ]
                }
            ],
            "types": []
        }
    }
}
```
