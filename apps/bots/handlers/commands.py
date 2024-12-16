from aiogram import Router, types, F
from aiogram.filters import Command

from ..keyboards.inline import inline_language_select

router = Router()


@router.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer(
        "Salom, Xush kelibsiz\nПривет, добро пожаловать\nHello, ur welcome",
    )


@router.message(Command("help"))
async def help_command(message: types.Message):
    await message.answer(
        "Available commands:\n/start - Start the bot\n/help - Get help"
    )
