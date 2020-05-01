import requests

def get_titles():
    # your code here
    titles = []
    response = requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")
    response = response.json()

    for item in range(0, len(response["posts"])):
        titles.append(response["posts"][item]["title"])

    return titles

print(get_titles())    