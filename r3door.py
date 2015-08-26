import json
import requests


def getStatusByName(data, name):
    try:
        return filter(lambda x: x['name'] == name, data['sensors']['door_locked'])[0]['value']
    except KeyError:
        return true


def getDoorstatus():
    resp = requests.get(url="http://realraum.at/status.json")
    data = resp.json()
    locked = getStatusByName(data, 'TorwaechterLock')
    kontakted = getStatusByName(data, 'TorwaechterAjarSensor')
    return (locked, kontakted)
