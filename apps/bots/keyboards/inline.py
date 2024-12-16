from aiogram.utils.keyboard import InlineKeyboardBuilder
from ..utils.callback_data import (
    LanguageSelectActions,
    cb_language_select_callback_data,
)


def inline_language_select():
    inline_keyboard = InlineKeyboardBuilder()

    inline_keyboard.button(
        text="uz Uzbek",
        callback_data=cb_language_select_callback_data(
            action=LanguageSelectActions.UZBEK
        ),
    )

    inline_keyboard.button(
        text="ru Russian",
        callback_data=cb_language_select_callback_data(
            action=LanguageSelectActions.RUSSIAN
        ),
    )

    inline_keyboard.button(
        text="en English",
        callback_data=cb_language_select_callback_data(
            action=LanguageSelectActions.ENGLISH
        ),
    )

    return inline_keyboard.as_markup()
