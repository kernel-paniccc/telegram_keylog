from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer("Это бот для хакинга школы. Не судите строго.\n/get_logs\n/clear_logs")


@router.message(Command("get_logs"))
async def logs(message: Message):
    with open("logfile.txt", 'r') as f:
        content = f.read()
    if len(content) == 0:
        await message.answer("Логов нет")
    else: await message.answer(str(content))


@router.message(Command("clear_logs"))
async def logs_clear(message: Message):
    with open("logfile.txt", 'w') as f:
        pass
    await message.answer("Логи очищенны !")


@router.message()
async def echo(messange: Message):
    await messange.answer('Я вас не понимаю. Используйте встроенные команды')