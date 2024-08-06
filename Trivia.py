
import requests
from pprint import pprint
import json

categories_url = "https://opentdb.com/api.php?amount=50"
response = requests.get(categories_url)

with open("Trivia.json", "w") as f:
    json.dump(response.json(), f , indent=4)