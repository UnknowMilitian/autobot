from enum import Enum
from aiogram.filters.callback_data import CallbackData


# ! --------------- Language select Callback troubles ---------------
class SelectLanguage(str, Enum):
    UZ = "uz"
    RU = "ru"
    EN = "en"


class SelectLanguageCallbackData(CallbackData, prefix="select_language"):
    language: SelectLanguage


def cb_select_language_callback_data(lang):
    return SelectLanguageCallbackData(language=lang.value).pack()


# ! --------------- Main menu Callback troubles ---------------
class MainMenuActions(str, Enum):
    NEW_DETECTION = "new_detection"
    ACTIVE_DETECTION = "active_detection"
    SETTINGS = "settings"


class MainMenuCallbackData(CallbackData, prefix="main_menu"):
    action: MainMenuActions


def cb_main_menu_select_callback_data(action):
    return MainMenuCallbackData(action=action.value).pack()
