import requests

def download_image(url: str):
    response = requests.get(url)
    with open("img.jpg", 'wb') as file:
        file.write(response.content)
