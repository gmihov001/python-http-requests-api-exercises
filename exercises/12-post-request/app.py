import requests

url = "https://assets.breatheco.de/apis/fake/sample/post.php"
my_info = {"monkey key": "monkey value"}
posted = requests.post(url, data = my_info)

print(posted.text)