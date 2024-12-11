from enum import Enum
from aiogram.filters.callback_data import CallbackData


class MainMenuActions(str, Enum):
    ORDER = "order"
    ABOUT = "about"
    MY_ORDERS = "my_orders"


class MainMenuCallbackData(CallbackData):
    action = MainMenuActions.value


def cb_main_menu_callback_data(action):
    return MainMenuCallbackData(action=action).pack()
