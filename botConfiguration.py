from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage

TOKEN =  '5391145092:AAFPd2wA9Dvza-DAXfd15COon8Atowfxk80'

bot = Bot(TOKEN)


dp = Dispatcher(bot, storage = MemoryStorage())