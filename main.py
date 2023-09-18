# @mansourshebli

from flask import Flask, render_template, jsonify

# https://docs.python.org/3/library/json.html
# This library will be used to parse the JSON data returned by the API.
import json

# https://docs.python.org/3/library/urllib.request.html#module-urllib.request
# This library will be used to fetch the API.
import urllib.request

# App configuration
app = Flask(__name__)
app.run(host="0.0.0.0", port=80)

# API get news function
def get_news():
    # Utilizing API key from GNews
    apikey = "910f4ef48b858659cf53b9f030a88c88"
    category = "general"
    url = f"https://gnews.io/api/v4/top-headlines?category={category}&lang=en&country=us&max=10&apikey={apikey}"

    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode("utf-8"))
        articles = data["articles"]

        # Create a list to store the news articles
        news_list = []

        for article in articles:
            news_item = {
                "title": article["title"],
                "description": article["description"],
                "url": article["url"],
                "image": article["image"],
                "publishedAt": article["publishedAt"],
                "source": article["source"]["name"]
            }
            news_list.append(news_item)

        return news_list

# Route to display news
@app.route("/")
def index():
    news_data = get_news()
    return render_template("index.html", news=news_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=500, debug=True)
