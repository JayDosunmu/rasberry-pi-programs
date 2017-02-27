import urllib.request

url = 'http://learning-api.herokuapp.com/number-list/'

with urllib.request.urlopen(url) as response:
    data = response.read()

print(data)
