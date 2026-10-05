import requests
from bs4 import BeautifulSoup
import pprint

response = requests.get("https://news.ycombinator.com/")
response2 = requests.get("https://news.ycombinator.com/?p=2")
good_soup = BeautifulSoup(response.text, "html.parser")
good_soup2 = BeautifulSoup(response2.text, "html.parser")

links = good_soup.select(".titleline")
subtext = good_soup.select(".subtext")
news_age = good_soup.select(".age")
links2 = good_soup2.select(".titleline")
subtext2 = good_soup2.select(".subtext")
news_age2 = good_soup2.select(".age")

mega_link = links + links
mega_subtext = subtext + subtext2
mega_news_age = news_age + news_age2


def sort_stories_by_votes(hn_list):
    return sorted(hn_list, key=lambda k: k["votes"], reverse=True)


def create_custom_hn(links, subtext, news_age):
    hn = []
    for index, link_item in enumerate(links):
        title = link_item.getText()
        href = link_item.a.get("href", None)
        vote = subtext[index].select(".score")
        age = news_age[index].getText()
        if len(vote):
            points = int(vote[0].getText().replace(" points", ""))
            if points > 99:
                hn.append({"title": title, "link": href, "votes": points, "age": age})

    return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hn(mega_link, mega_subtext, mega_news_age))
