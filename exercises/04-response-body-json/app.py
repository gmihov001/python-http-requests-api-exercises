import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/time.php")
print(response.text)

print(response.json())

print(type(response.json()))