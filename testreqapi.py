import requests

url = 'http://127.0.0.1:8000/hello/'
headers = {'Authorization': 'Token 84f543011f0fa300b93040c74f55cf1557e89bc2'}
r = requests.get(url, headers=headers)
print(r.text)