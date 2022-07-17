import requests
from aiogram import types, executor, Dispatcher, Bot #библиотека для бота
from bs4 import BeautifulSoup
import fake_useragent

user = fake_useragent.UserAgent().random
header = {'user-agent': user}

#подмена юзер-агента
user = fake_useragent.UserAgent().random 
header = {'user-agent': user} 

# top rating
url = "https://www.kinoafisha.info/rating/movies/"
responce = requests.get(url, headers=header).text 
soup = BeautifulSoup(responce, 'html.parser')

all_links = soup.find_all('a', class_='movieItem_title')
for link in all_links:
    url = link["href"]

    position = link.find_parent('div', class_="movieItem_info")
    position = position.findChildren('span', class_="movieItem_position")

    movieItem_details = link.find_parent('div', class_="movieItem_info")
    movieItem_details = movieItem_details('div', class_="movieItem_details")

    for pos in position:
        print(pos.text)
    print(url)
    print(link.text)
    for details in movieItem_details:
        print(details.text)

    if all_links.index(link) == 9:
        break

    picture = soup.find('img', class_='picture_image')
    picture = picture["data-picture"]
    print(picture)
    
"""all_pictures = soup.find_all('img', class_='picture_image')
for picture in all_pictures:
    picture = picture["data-picture"]
    print(picture)
    if all_links.index(link) == 9:
        break"""

"""movieItem_info = soup.find_all("div", class_="movieItem_info")
for movieItem in movieItem_info:
    print(movieItem.text)"""
