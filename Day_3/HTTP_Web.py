import http.client
import json

r = http.client.HTTPConnection('api.football-data.org')
headers = {'Content-type':'application/json',
             'Accept':'application/json','X-Response-Control': 'minified'}
r.request('GET', '/v1/teams/66/', None, headers )
result = json.loads(r.getresponse().read().decode())

print (result)
