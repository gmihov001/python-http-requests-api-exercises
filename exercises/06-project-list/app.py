import requests

# your code here

response = requests.get("https://assets.breatheco.de/apis/fake/sample/project_list.php")
response = response.json()

print(response[1]["name"])