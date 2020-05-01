import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/time.php")
response = response.json()

print(response)


print("Current time: " + response["hours"] + " hrs " + response["minutes"] + " min and " + response["seconds"] + " sec")
