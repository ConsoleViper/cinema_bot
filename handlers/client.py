from aiogram import Dispatcher
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from botConfiguration import dp, bot 
from handlers.keyboards.clientKB import main_keyboard, movie_kb

class ClientForm(StatesGroup):
    client_offer = State()

async def welcomer(message : types.Message):
    await bot.send_message(message.from_user.id, 'Hi, I\'m cinema bot. What do you want?', reply_markup=main_keyboard)

# работа с вторичным меню
async def second_menu(message : types.Message):
    if message.text == 'Подивитися фільми':
        await bot.send_message(message.from_user.id, 'Подивитися фільми', reply_markup=movie_kb)
    elif message.text == "В головне меню":
        await bot.send_message(message.from_user.id, 'Головне меню', reply_markup=main_keyboard)
    elif message.text == 'Приєднатися до команди':
        await work_offer(message)


async def work_offer(message: types.Message):
    await ClientForm.client_offer.set()
    await bot.send_message(message.from_user.id, 'Якщо ти вирішив приєднатися до нашої команди, то надішли документ(docx, pdf) з такими критеріями:\nтвоє фото, ПІБ, дата народження, досвід роботи та контактний номер телефону')

async def upload_form(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['client_offer'] = message.answer_document
    


def register_handlers_client(dp : Dispatcher):
    
    dp.register_message_handler(welcomer, commands=['start'])
    dp.register_message_handler(second_menu)
    