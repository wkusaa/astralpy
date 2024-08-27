import time
import requests
import astralpy
from rich.progress import track
from rich.pretty import pprint


for i in track(range(20), description="For example:"):
    time.sleep(0.05)


resp = requests.get("https://peps.python.org/api/peps.json")
data = resp.json()
pprint([(k, v["title"]) for k, v in data.items()][:10])

print(astralpy.hello())