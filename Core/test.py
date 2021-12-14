import requests
import json
url = "https://login.microsoftonline.com/fdb969dd-87c5-4a41-87d6-86f80f4581db/oauth2/token"
clientid= "920ce63d-e9bb-4d4a-ae38-ffec210bcb0e"
payload = 'grant_type=client_credentials&client_id=920ce63d-e9bb-4d4a-ae38-ffec210bcb0e&client_secret=EkLs1-1W~KM46g8UG7Hj6g-kguCR-ik0v3&resource=2ff814a6-3304-4ab8-85cb-cd0e6f879c1d'
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
response = requests.request("POST", url, headers=headers, data = payload)
bear = json.loads(response.text.encode('utf8'))
bearertoken = json.dumps(bear['access_token'])
tokentype = json.dumps((bear['token_type']))
pickytoken = tokentype.translate({ord('"'): None}) +" "+bearertoken.translate({ord('"'): None})
#print(bearertoken)
print(pickytoken)

#grant_type=client_credentials&client_id=<client-id>&resource=2ff814a6-3304-4ab8-85cb-cd0e6f879c1d&client_secret=<application-secret>' \
