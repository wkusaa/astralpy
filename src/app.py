import os
import requests

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    """Example Hello World route."""
    print(os.getenv("FLASK_APP"))
    resp = requests.get("https://peps.python.org/api/peps.json")
    data = resp.json()
    return f"{data}"


if __name__ == "__main__":
    app.run(debug=True, port=int(os.getenv("PORT", 8080)))