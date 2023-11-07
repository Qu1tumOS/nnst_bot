from aiogram.types import InlineKeyboardButton
from config_data.config import payment_url
from aiogram.utils.keyboard import InlineKeyboardBuilder


buttons = [
    InlineKeyboardButton(
        text="меню",
        callback_data='menu_button'
    ),

    InlineKeyboardButton(
        text="💵",
        url=payment_url()
    )
]

Pay_keyboard = InlineKeyboardBuilder().row(*buttons, width=2).as_markup()
