import requests
from aiogram import types, executor, Dispatcher, Bot
from bs4 import BeautifulSoup
import fake_useragent

user = fake_useragent.UserAgent().random
header = {'user-agent': user}


bot = Bot("")
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message: types.message):
    await bot.send_message(message.chat.id, "привет",
                           parse_mode="html", disable_web_page_preview=1 )


@dp.message_handler(commands='top')
async def start(message: types.message):
    link = "https://www.kinoafisha.info/rating/movies/"
    responce = requests.get(link, headers=header).text
    soup = BeautifulSoup(responce, 'html.parser')
    block_title = soup.find_all('a', class_='movieItem_title')
    block_genre = soup.find_all('span', class_='movieItem_genres')
    films = []
    itop = 1
    for title, genres in zip(block_title, block_genre):
        films += str(itop) + '. '
        films += title.findAll(text=True)
        films += "\n"
        films += genres.findAll(text=True)
        films += "\n"
        answer = ' '.join(films)
        await bot.send_message(message.chat.id, answer,
                               parse_mode="html")
        films.clear()
        itop += 1
        if block_title.index(title) == 9:
            break
        #await bot.send_photo(message.chat.id, block_picture)


executor.start_polling(dp)
