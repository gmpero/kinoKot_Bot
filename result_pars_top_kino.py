import requests
from bs4 import BeautifulSoup
import fake_useragent

user = fake_useragent.UserAgent().random
header = {'user-agent': user}

user = fake_useragent.UserAgent().random
header = {'user-agent': user}

# top rating
url = "https://www.kinoafisha.info/rating/movies/"
responce = requests.get(url, headers=header).text
soup = BeautifulSoup(responce, 'html.parser')

all_links = soup.find_all('div', class_='movieList_item')
for link in all_links:
    # search movieItem_posters
    movieItem_posters = link.find('img', class_='picture_image')
    movieItem_posters = movieItem_posters["data-picture"]

    # search movieItem_details
    movieItem_details = link.find('div', class_="movieItem_info")
    movieItem_details = movieItem_details('div', class_="movieItem_details")

    # search movieItem_title
    movieItem_title = link.find('div', class_="movieItem_info")
    movieItem_title = movieItem_title('a', class_="movieItem_title")

    # search position_movie
    position = link.find('div', class_="movieItem_info")
    position = position.findChildren('span', class_="movieItem_position")

    # print info
    for pos in position:
        print(pos.text)
    for title in movieItem_title:
        url = title["href"]
        print(url)
        print(title.text)

    for detail in movieItem_details:
        print(detail.text)
    print(movieItem_posters)

    print("")
    if all_links.index(link) == 9:
        break
