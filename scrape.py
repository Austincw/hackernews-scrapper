import requests
from bs4 import BeautifulSoup
import pprint

response = requests.get("https://news.ycombinator.com/")
good_soup = BeautifulSoup(response.text, "html.parser")
links = good_soup.select(".titleline")
subtext = good_soup.select(".subtext")


def create_custom_hn(links, subtext):
    hn = []
    for index, link_item in enumerate(links):
        title = link_item.getText()
        href = link_item.a.get("href", None)
        vote = subtext[index].select(".score")
        if len(vote):
            points = int(vote[0].getText().replace(" points", ""))
            if points > 99:
                hn.append({"title": title, "link": href, "votes": points})

    return hn


pprint.pprint(create_custom_hn(links, subtext))
