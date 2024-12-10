from aiogram import Router, types, F
from aiogram.filters import Command


router = Router()


@router.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer("Hello, I'm a simple bot")


@router.message(Command("help"))
async def help_command(message: types.Message):
    await message.answer(
        "Available commands:\n/start - Start the bot\n/help - Get help"
    )
