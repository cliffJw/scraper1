from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from colorama import Fore, Back, Style
import requests, string, re


def hackernews():
    ua = UserAgent()
    header = {'User-Agent': str(ua.chrome)}
    link = ["https://thehackernews.com"]
    for link in link:
        response = requests.get(link, timeout=5, headers=header)
        soup = BeautifulSoup(response.content, "html.parser")
        title_list = []
        content_list = []
        date_list = []
        links_list = []
        for links in soup.find_all('h2', attrs={"class": "home-title"}):
            title = ''.join(x for x in links.text if x in string.printable).strip()
            title_list.append(title)
            # print(f'TITLE : {title}')
        for links in soup.find_all('div', attrs={"class": "home-desc"}):
            content = ''.join(x for x in links.text if x in string.printable).strip()
            content_list.append(content)
            # print(f'CONTENT  : {content}')
        for links in soup.find_all('div', attrs={"class": "item-label"}):
            da = ''.join(x for x in links.text if x in string.printable).strip()
            date_list.append(da)
            # print(f'Date & author  : {da}')

        for links in soup.find_all('a', attrs={"class": "story-link"}):
            link = links.get('href')
            links_list.append(link)
            # print(f'Link  : {link}')
        if len(title_list)==len(content_list)==len(date_list)==len(links_list):
            items = len(content_list)
            title_list=list(reversed(title_list))
            content_list=list(reversed(content_list))
            date_list=list(reversed(date_list))
            links_list=list(reversed(links_list))

            for i in title_list:
                title = title_list[title_list.index(i)] 
                content = content_list[title_list.index(i)]
                date = date_list[title_list.index(i)]
                news_url = links_list[title_list.index(i)]

                print(f'Title: {title}, \n Content: {content}, \n Date : {date} \n Links: {news_url}')

            
      

    
hackernews()
