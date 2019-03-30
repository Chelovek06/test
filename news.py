import requests
import bs4

def get_news():
    url = "https://news.mail.ru"
    content = requests.get(url).content
    soup = bs4.BeautifulSoup(content, "lxml")
    return soup.find_all("a", {"class": "list__text"})

def format_news():
    news_tags = get_news()

    result = ""

    for news in news_tags:
        result += news.text + "\n"

    return result
