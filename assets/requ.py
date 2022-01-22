# Imports

from operator import indexOf
import requests
from datetime import timezone
import datetime
import secrets
from config import *


random_hex = secrets.token_hex(18)
print(random_hex)
random_hex_2 = secrets.token_hex(18)
print(random_hex_2)

def timestamp():
    dt = datetime.datetime.now(timezone.utc)
    utc_timestamp = dt.replace(tzinfo=timezone.utc)
    utc_timestamp = utc_timestamp.timestamp()
    utc_timestamp = str(utc_timestamp)
    point = utc_timestamp.find('.')
    utc_timestamp = list(utc_timestamp)
    utc_timestamp[point] = ''
    for i in range (1, 4):
        utc_timestamp[-1 * i] = ''
    utc_timestamp = ''.join(utc_timestamp)
    if len(utc_timestamp) == 12:
        utc_timestamp = utc_timestamp + '0'
    print(utc_timestamp)
    print(len(utc_timestamp))
    return utc_timestamp

_link = 'https://api2.nicehash.com/main/api/v2/mining/algo/stats'

_headers = {
    'X-Time': timestamp(),
    'X-Nonce': random_hex,
    'X-Organization-Id' : ORG_ID,
    'X-Request-Id' : random_hex_2
}

r = requests.get(_link, headers=_headers)
print(r.text)
