from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from botConfiguration import bot, dp
from .keyboards import adminKb, clientKB

_ADMIN_PASS = 'peoplevolkondatrnews'

async def cancel_work(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await message.reply('Cancel work')
    await state.finish()

class Admin(StatesGroup):
    try_pass = State()

async def admin_check(message: types.Message):
    await Admin.try_pass.set()
    await message.reply('Enter admin password')

async def enter_pass(message: types.Message, state: FSMContext):
    if message.text.lower() == _ADMIN_PASS:
        async with state.proxy() as data:
            data['try_pass'] = message.text
        await bot.send_message(message.from_user.id, 'Перевірка пройдена!', reply_markup=adminKb.mainkb_admin)
        await state.finish()
    else:
        await bot.send_message(message.from_user.id, 'Спробуйте ще раз! Або введіть "cancel"')


# Робота з меню адміна 
async def add_film(message: types.Message):
    await bot.send_message(message.from_user.id, 'Додаємо...') # Прийти і зробити класс фільму через FSM та підключити бд 

async def admin_exit(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вихід...', reply_markup=clientKB.main_keyboard)


def register_handlers_admin(dp : Dispatcher):
    
    dp.register_message_handler(cancel_work, commands=['cancel'], state='*')
    dp.register_message_handler(cancel_work, Text(equals='cancel', ignore_case = True), state="*")

    dp.register_message_handler(admin_check, commands=['admin'], state=None)
    dp.register_message_handler(enter_pass, state=Admin.try_pass)
    dp.register_message_handler(add_film, Text(ignore_case=True, equals='Додати фільм'))
    dp.register_message_handler(admin_exit, Text(ignore_case=True, equals='В головне меню(вийти з адмінки)'))