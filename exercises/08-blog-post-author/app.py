import requests

# your code here

response = requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")

response = response.json()

print(response["posts"][0]["author"]["name"])