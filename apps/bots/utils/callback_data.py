from enum import Enum
from aiogram.filters.callback_data import CallbackData


class LanguageSelectActions(str, Enum):
    UZBEK = "uzbek"
    RUSSIAN = "russian"
    ENGLISH = "english"


class LanguageSelectCallbackData(CallbackData, prefix="select_language"):
    language: LanguageSelectActions


def cb_language_select_callback_data(lang):
    return LanguageSelectCallbackData(language=lang.value).pack()
