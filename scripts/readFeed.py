import feedparser

def execute(url):
    feed = feedparser.parse(url, agent='Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion')
    return feed['items']
