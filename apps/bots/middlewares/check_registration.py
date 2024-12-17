from aiogram.types import Update
from aiogram import BaseMiddleware, Bot, types

from typing import Callable, Dict, Any, Awaitable
from apps.bots.keyboards.inline import inline_languages
from apps.bots.utils.states import MenuStateGroup, RegistrationStateGroup

EVENT_FROM_USER = "event_from_user"

from apps.bots.models import User


class CheckRegistrationMiddleware(BaseMiddleware):

    async def __call__(
        self,
        handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
        event: Update,
        data: Dict[str, Any],
    ) -> Any:
        bot: Bot = data["bot"]
        user: User = data.get(EVENT_FROM_USER)
        state = data["state"]

        current_state = await state.get_state()

        user_obj = await User.objects.filter(telegram_id=user.id).afirst()

        print(current_state, MenuStateGroup.__all_states__)

        if not user_obj and not current_state in RegistrationStateGroup.__all_states__:
            await bot.send_message(
                chat_id=user.id,
                text="Iltimos avval registratsiyadan o`ting",
                reply_markup=types.ReplyKeyboardRemove(),
            )
            await state.set_state(RegistrationStateGroup.language)
            return await bot.send_message(
                chat_id=user.id,
                text="Tilni tanlang",
                reply_markup=inline_languages(),
            )

        data["user"] = user_obj

        return await handler(event, data)


__all__ = ["CheckRegistrationMiddleware"]
