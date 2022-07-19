from aiogram import executor
from botConfiguration import dp
from handlers import client

async def checkWork(_):
    print("Bot is working")

client.register_handlers_client(dp = dp)

executor.start_polling(skip_updates = True,dispatcher = dp, on_startup=checkWork)