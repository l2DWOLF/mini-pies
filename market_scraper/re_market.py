import requests 

url = 'https://opentdb.com/api.php?amount=10'

response = requests.get(url)
res_json = response.json()
print(res_json['results'][0])
