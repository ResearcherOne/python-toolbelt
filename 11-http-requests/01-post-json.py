import requests
import simplejson as json

url = "http://ip:port"
data = {'auth_token': 'auth1', 'widget': 'id1', 'title': 'Something1', 'text': 'Some text', 'moreinfo': 'Subtitle'}
headers = {'Content-type': 'application/json'}
r = requests.post(url, data=json.dumps(data), headers=headers)
