import requests
import json
import datetime
import homeassistant.remote as remote

mindergas = 'http://www.mindergas.nl/api/gas_meter_readings'
mindergas_token = 'XXXXXXXXXXXXXXXXXXXX'
hass_ip = '127.0.0.1'
hass_password = ''
hass_port = '8123'
gas_sensor = 'sensor.gas_consumption'
api = remote.API(hass_ip,hass_password, hass_port)
gas_usage = remote.get_state(api, 'sensor.gas_consumption')

def post():
    yesterday = datetime.date.today () - datetime.timedelta (days=1)
    data = {'date': yesterday.strftime ("%Y%m%d"), 'reading':gas_usage.state}
    headers = {'Content-Type': 'application/json', 'AUTH-TOKEN': mindergas_token}
    r = requests.post(mindergas, data=json.dumps(data), headers=headers)
    print (yesterday.strftime ("%Y%m%d"))
    print (data)
    print (r)
    print ('Ready')

post()
