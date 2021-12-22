# import required modules
from bs4 import BeautifulSoup
import requests

# get URL
url="https://en.wikipedia.org/wiki/N"

# scrape webpage

def wikibot(url):
    url_open=requests.get(url)
    soup = BeautifulSoup(url_open.content, 'html.parser')
    details=soup('table',{'class':'infobox'})
    for i in details:
        h=i.find_all("tr")
        for j in h:
            heading=j.find_all("th")
            detail=j.find_all("td")
            if heading is not None and detail is not None:
                for x,y in zip(heading,detail):
                    print("{}  ::   {}".format(x.text,y.text))
                    print("-"*100)
    for i in range(1,3):
        print(soup('p')[i].text)
    print("1.History\n2.Use in Writting Systems\n3.Other Uses\nEnter your option:")
    x=int(input())
    print(soup('p')[x+1].text)
wikibot(url)