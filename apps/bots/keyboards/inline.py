from aiogram.utils.keyboard import InlineKeyboardBuilder
from apps.bots.utils.callback_data import cb_main_menu_callback_data, MainMenuActions


def inline_main_menu():
    inline_keyboard = InlineKeyboardBuilder()

    inline_keyboard.button(
        text="Buyurtma berish",
        callback_data=cb_main_menu_callback_data(action=MainMenuActions.ORDER),
    )

    return (
        keyboard.row(order_button, about_button)
        .row(my_orders_button, branches_button)
        .row(settings_button)
    )
