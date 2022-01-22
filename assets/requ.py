import requests
from datetime import timezone
import datetime
import hmac
import hashlib
import config
import secrets

RIG_ID = "0-RvS1zVH3b0C1xX7KmUIlMQ"

def utc_timestamp() -> str:
    dt = datetime.datetime.now(timezone.utc)
    utc_time = dt.replace(tzinfo=timezone.utc)
    utc_timestamp = utc_time.timestamp()
    
    utcarr = str(utc_timestamp).split('.')
    utcinms = utcarr[0] + utcarr[1][:3]
    return utcinms
    # return str(utc_timestamp).split('.')[0]


nicehash_api = "https://api2.nicehash.com"
rig_statistics = "/main/api/v2/mining/rig/stats/algo"
params = f"rigId={RIG_ID}&algorithm=20"

_headers = {
    "X-Time": utc_timestamp(),
    "X-Nonce": secrets.token_hex(18),
    "X-Organization-Id": config.ORG_ID,
    "X-Request-Id": secrets.token_hex(16),
}

# signing from here
xauthinput = bytes(config.API_KEY, 'utf-8')
xauthinput += bytes([0x00])
xauthinput += bytes(_headers['X-Time'], 'utf-8')
xauthinput += bytes([0x00])
xauthinput += bytes(_headers['X-Nonce'], 'utf-8')
xauthinput += bytes([0x00])
xauthinput += bytes([0x00])
xauthinput += bytes(config.ORG_ID, 'utf-8')
xauthinput += bytes([0x00])
xauthinput += bytes([0x00])
xauthinput += bytes("GET", 'utf-8')
xauthinput += bytes([0x00])
xauthinput += bytes(rig_statistics, 'utf-8')
xauthinput += bytes([0x00])
xauthinput += bytes(params, 'utf-8')
xauth = hmac.new(bytes(config.SECRET_KEY, 'utf-8'), msg=xauthinput, digestmod=hashlib.sha256).hexdigest()
xauth = config.API_KEY + ':' + xauth
_headers['X-Auth'] = xauth


r = requests.get(url=(nicehash_api + rig_statistics + '?' + params), headers=_headers)

print(r.text)
