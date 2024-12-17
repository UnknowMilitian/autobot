from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext


from apps.bots.keyboards.inline import show_main_menu


router = Router()


@router.message(Command("start"))
async def start_command(message: types.Message, state=FSMContext):
    await message.answer("Quyidagilardan birini tanlang", reply_markup=show_main_menu())


@router.message(Command("help"))
async def help_command(message: types.Message):
    await message.answer(_("Bor komandalar: \nstart - Start the bot\n/help - Get help"))
