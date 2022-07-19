from aiogram.types.reply_keyboard import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup

# Main keyboard
#buy_tickets = KeyboardButton('Придбати квитки') Потім буде так, виводиться інлайн кнопка під кожним фільмом з надписом
# "придбати квитки" яка веде на сторінку фільму на сайті 

movies = KeyboardButton('Подивитися фільми')
work_offer = KeyboardButton('Приєднатися до команди')

main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(movies).add(work_offer)


# Keyboard if you looking for a film
present_films = KeyboardButton('Фільми які йдуть зараз')
future_films = KeyboardButton('Анонси фільмів')
m_menu = KeyboardButton('В головне меню')

movie_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(present_films).add(future_films).add(m_menu)