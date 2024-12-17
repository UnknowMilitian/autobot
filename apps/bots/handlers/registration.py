import django

django.setup()

from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from apps.bots.keyboards.reply import reply_send_phone_number
from apps.bots.utils.states import RegistrationStateGroup
from apps.bots.utils.callback_data import SelectLanguageCallbackData
from apps.bots.models import User
from apps.bots.handlers.commands import start_command

router = Router()


@router.callback_query(SelectLanguageCallbackData.filter())
async def start_order(
    callback_query: types.CallbackQuery,
    state: FSMContext,
    callback_data: SelectLanguageCallbackData,
):
    await state.update_data({"language": callback_data.language})

    await callback_query.message.answer(
        "Telefon raqamingizni jo`nating", reply_markup=reply_send_phone_number()
    )
    await state.set_state(RegistrationStateGroup.phone)


@router.message(F.text, RegistrationStateGroup.phone)
async def receive_phone(message: types.Message, state: FSMContext):
    if not message.text.startswith("+998") or len(message.text) != 13:
        return await message.answer(
            "To`g`ri formatda raqam jo`nating yoki buttondan foydalaning"
        )

    await state.update_data({"phone_number": message.text})
    await state.set_state(RegistrationStateGroup.name)
    await message.answer(
        "Ismingizni jo`nating", reply_markup=types.ReplyKeyboardRemove()
    )


@router.message(F.contact, RegistrationStateGroup.phone)
async def receive_contact(message: types.Message, state: FSMContext):
    await state.update_data({"phone_number": message.contact.phone_number})
    await state.set_state(RegistrationStateGroup.name)
    await message.answer(
        "Ismingizni jo`nating", reply_markup=types.ReplyKeyboardRemove()
    )


@router.message(F.text, RegistrationStateGroup.name)
async def receive_name(message: types.Message, state: FSMContext):
    await state.update_data({"name": message.text})
    registration_data = await state.get_data()

    await message.answer(
        f"Sizning ismingiz: {registration_data['name']}\n"
        f"Telefon raqamingiz: {registration_data['phone_number']}\n"
        f"Tiliz: {registration_data['language']}\n\n"
        "Sizning registratsiyani yakunlashingiz uchun tugmasini bosing"
    )

    # Foydalanuvchini bazaga qo'shish
    await User.objects.acreate(
        telegram_id=message.from_user.id,
        username=registration_data["name"],
        phone_number=registration_data["phone_number"],
        language=registration_data["language"],
    )

    await state.clear()
    await start_command(message, state)
