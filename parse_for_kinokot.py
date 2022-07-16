import requests
from aiogram import types, executor, Dispatcher, Bot
from bs4 import BeautifulSoup
import fake_useragent

user = fake_useragent.UserAgent().random
header = {'user-agent': user}


user = fake_useragent.UserAgent().random
header = {'user-agent': user}
# top rating
"""link = "https://www.kinoafisha.info/rating/movies/"
responce = requests.get(link, headers=header).text
soup = BeautifulSoup(responce, 'html.parser')
block_title = soup.find_all('a', class_='movieItem_title')
block_genre = soup.find_all('span', class_='movieItem_genres')
block_picture = soup.find_all('img', class_='picture_image')
for link in block_picture:
    block_picture = block_picture['src']
    print(link)"""
'''films = []
for title, genres in zip(block_title, block_genre):
    films += title.findAll(text=True)
    films += genres.findAll(text=True)
    print(films)
    films.clear()'''

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

"""movieItem_info = soup.find_all("div", class_="movieItem_info")
for movieItem in movieItem_info:
    print(movieItem.text)"""
