import requests

def get_post_tags(post_id):
    tags = []
    response = requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")
    response = response.json()

    for item in range(0, len(response["posts"])):
        if response["posts"][item]["id"] == post_id:
            for item in response["posts"][item]["tags"]:
                tags.append(item)

    return tags


print(get_post_tags(146))