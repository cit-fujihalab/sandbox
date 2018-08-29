import json
import requests

odpt = "BusTimetable"
accses_token = "1ac4a44dbef3800a5c95c1abaccf2be489a3308c7515670d884f803026a17adc"
url = "https://api-tokyochallenge.odpt.org/api/v4/odpt:{0}?acl:consumerKey={1}".format(odpt, accses_token)

response = requests.get(url)
data = response.json()

print(url)
