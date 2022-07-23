from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram import types
from botConfiguration import dp, bot 
from handlers.keyboards.clientKB import main_keyboard, movie_kb

# not working
async def cancel_work(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await message.reply('Cancel work')
    await state.finish()

async def starter(message : types.Message):
    await bot.send_message(message.from_user.id, f'Hi, I\'m cinema bot.\nWhat do you want?', reply_markup=main_keyboard)

async def watching_films(message : types.Message):
    await bot.send_message(message.from_user.id, 'Подивитися фільми', reply_markup=movie_kb)

async def team_join(message: types.Message):
    await work_offer(message)

async def go_to_mainMenu(message: types.Message):
    await bot.send_message(message.from_user.id, 'Головне меню', reply_markup=main_keyboard)

async def work_offer(message: types.Message):
    await bot.send_message(message.from_user.id, 'Якщо ти вирішив приєднатися до нашої команди, то надішли документ(docx, pdf) з даними:\nВаше фото, ПІБ, дата народження, досвід роботи та контактний номер телефону')


def register_handlers_client(dp : Dispatcher):

    dp.register_message_handler(cancel_work, commands=['cancel'], state="*")
    dp.register_message_handler(cancel_work, Text(ignore_case=True, equals='cancel'), state = '*')
    
    dp.register_message_handler(starter, commands=['start'])
    dp.register_message_handler(watching_films, Text(ignore_case=True, equals='Подивитися фільми'))
    dp.register_message_handler(team_join, Text(ignore_case=True, equals='Приєднатися до команди'))
    dp.register_message_handler(go_to_mainMenu, Text(ignore_case=True, equals='В головне меню'))
    

    