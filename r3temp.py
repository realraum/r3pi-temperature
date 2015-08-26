import requests
import json


def loadTemp():
    tfile = open("/sys/bus/w1/devices/10-000801375be4/w1_slave")
    text = tfile.read()
    tfile.close()
    secondline = text.split("\n")[1]
    temperaturedata = secondline.split(" ")[9]
    temperature = float(temperaturedata[2:])
    temperature = temperature / 1000
    return temperature


def getTempFromSensor():
    while True:
        temp = loadTemp()
        if temp < 85:
            break
    return temp


def getTempByName(data, name):
    try:
        return filter(lambda x: x['name'] == name, data['sensors']['temperature'])[0]['value']
    except KeyError:
        return 42


def getTemp():
    resp = requests.get(url="http://realraum.at/status.json")
    data = resp.json()
    return getTempByName(data, 'Temp1')
