# @mansourshebli

from flask import Flask

app = Flask(__name__)

# using python decorator to add functionality to the website
@app.route("/apple-news")
def index():
    return "Apple News!"

app.run(host="0.0.0.0", port=80)