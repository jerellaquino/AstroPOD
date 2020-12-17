import json
from flask import Flask, render_template
import requests 

app = Flask(__name__)

key = "y6Mel6VDbUm0BiQMXhpSTREXao1DaQNl4a8rYsBe"

@app.route('/')
def AstroPic():

    base_url = "https://api.nasa.gov/planetary/apod?api_key=y6Mel6VDbUm0BiQMXhpSTREXao1DaQNl4a8rYsBe"
    r = requests.get(base_url)
    apod = r.json()

    return render_template("index.html", apod = apod)


if __name__ == "__main__":
    app.run()