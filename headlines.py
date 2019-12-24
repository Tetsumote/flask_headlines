import feedparser
from flask import Flask 

app = Flask(__name__)

RSS_FEEDS = {
    'bbc':'http://feeds.bbci.co.uk/news/rss.xml',
    'world':'http://feeds.bbci.co.uk/news/world/rss.xml',
    'tech':'http://feeds.bbci.co.uk/news/science_and_environment/rss.xml',
}
    

@app.route("/")
@app.route("/bbc")
def bbc():
    return get_news('bbc')

@app.route("/world")
def world():
    return get_news('world')

@app.route("/tech")
def tech():
    return get_news('tech')



def get_news(publication):
    feed = feedparser.parse(RSS_FEEDS[publication])
    first_article = feed['entries'][0]
    return """
    <html>
    <body>
    <h1> BBC Headlines </h1>
    <b>{0}</b><br/>
    <i>{1}</i><br/>
    <p>{2}</p><br/>
    </body>
    </html>
    """.format(first_article.get("title"),first_article.get("published"),first_article.get("summary"))


if __name__ == '__main__':
    app.run(port=5000, debug=True)