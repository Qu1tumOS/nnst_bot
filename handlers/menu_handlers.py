from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from keyboards.keyboard_creator import create_inline_kb



router = Router()


menu_keyboard = create_inline_kb(2, 'today_pars_button', 'tomorrow_pars_button', 'user_info')

text_menu = 'Главное меню\nпосмотреть расписание на:'

@router.message(Command(commands='menu'))
async def menu(message: Message):
    await message.answer(
        text=text_menu,
        reply_markup=menu_keyboard
    )


@router.callback_query(F.data == 'menu_button')
async def menu(callback: CallbackQuery):
    await callback.message.edit_text(
        text=text_menu,
        reply_markup=menu_keyboard
    )