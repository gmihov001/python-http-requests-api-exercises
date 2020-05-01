import requests

def get_attachment_by_id(attachment_id):
    
    attached = ''
    response = requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")
    response = response.json()

    for post_index in range(0, len(response["posts"])):

        for attachment in response["posts"][post_index]["attachments"]:

            if attachment["id"] == attachment_id:
                attached = str(attachment["title"])

    return attached

print(get_attachment_by_id(137))