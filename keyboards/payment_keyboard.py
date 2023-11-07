from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config_data.config import payment_url
from aiogram.utils.keyboard import InlineKeyboardBuilder
from keyboards.keyboard_creator import create_inline_kb

URL = payment_url()

# url_button_1 = InlineKeyboardButton(
#     text="тыкни чтоб накинуть ;)",
#     url=URL
# )
# menu_button_2 = InlineKeyboardButton(
#     text="меню",
#     callback_data='menu_button_1_pressed'
# )

# Pay_keyboar = InlineKeyboardMarkup(
#     inline_keyboard=[[url_button_1],
#                      [menu_button_2]]
# )

# -----------------------------------------------------------------------------------------------------------------------------------

buttons = [
    InlineKeyboardButton(
        text="меню",
        callback_data='menu_button_1_pressed'
    ),

    InlineKeyboardButton(
        text="💵",
        url=URL
    )
]

Pay_keyboard = InlineKeyboardBuilder().row(*buttons, width=2).as_markup()
