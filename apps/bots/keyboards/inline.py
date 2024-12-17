from aiogram.utils.keyboard import InlineKeyboardBuilder
from apps.bots.utils.callback_data import (
    SelectLanguage,
    cb_select_language_callback_data,
    MainMenuActions,
    cb_main_menu_select_callback_data,
)


def inline_languages():
    inline_keyboard = InlineKeyboardBuilder()
    inline_keyboard.button(
        text="Uzbek",
        callback_data=cb_select_language_callback_data(lang=SelectLanguage.UZ),
    )
    inline_keyboard.button(
        text="Russian",
        callback_data=cb_select_language_callback_data(lang=SelectLanguage.RU),
    )
    inline_keyboard.button(
        text="English",
        callback_data=cb_select_language_callback_data(lang=SelectLanguage.EN),
    )

    inline_keyboard.adjust(1)

    return inline_keyboard.as_markup()


def show_main_menu():
    inline_keyboard = InlineKeyboardBuilder()

    inline_keyboard.button(
        text="🔍 Create New Detection",
        callback_data=cb_main_menu_select_callback_data(
            action=MainMenuActions.NEW_DETECTION
        ),
    )

    inline_keyboard.button(
        text="📋 Active Detections",
        callback_data=cb_main_menu_select_callback_data(
            action=MainMenuActions.ACTIVE_DETECTION
        ),
    )

    inline_keyboard.button(
        text="⚙️ Settings",
        callback_data=cb_main_menu_select_callback_data(
            action=MainMenuActions.SETTINGS
        ),
    )

    inline_keyboard.adjust(2)
    return inline_keyboard.as_markup()
