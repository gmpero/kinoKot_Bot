import requests
from aiogram import types, executor, Dispatcher, Bot
from bs4 import BeautifulSoup
import fake_useragent

user = fake_useragent.UserAgent().random
header = {'user-agent': user}


bot = Bot("5537480841:AAEIa4auOoqWxptMrx3qgDHuDv34KfBkxWY")
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message: types.message):
    await bot.send_message(message.chat.id, "привет я кот мррр кино бот \n "
                                            "введи команду /top чтобы увидеть лучшие шедевры \n "
                                            "и да не пугайся я еще в разработке мяу", parse_mode="html")


@dp.message_handler(commands='top')
async def top_parser(message: types.message):
    films = []
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
        for pos, title, detail in zip(position, movieItem_title, movieItem_details):
            url = title["href"]
            films += "№" + pos.text + " "
            films += title.text
            films += detail.text
            films += url
            answer = ''.join(films)

            await bot.send_photo(message.chat.id, movieItem_posters, caption=answer)
            films.clear()
            if all_links.index(link) == 9:
                break
        if all_links.index(link) == 9:
            break
            
executor.start_polling(dp)
