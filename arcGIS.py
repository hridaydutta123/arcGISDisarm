import requests # pip install requests

# generate a token with your client id and client secret
token = requests.post('https://www.arcgis.com/sharing/rest/oauth2/token/', params={
  'f': 'json',
  'client_id': 'sWKwYe3QBg569xWj',
  'client_secret': '28b68ad512b64191bafe8cf45271fc35',
  'grant_type': 'client_credentials',
  'expiration': '1440'
})

print(token.json()['access_token']);

data = requests.post('http://geoenrich.arcgis.com/arcgis/rest/services/World/GeoenrichmentServer/Geoenrichment/enrich', params={
  'f': 'json',
  'token': token.json()['access_token'],
  'studyAreas': '[{"geometry":{"x":-117.1956,"y":34.0572}}]'
})

print(data.json())	