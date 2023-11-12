from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from parser.parser import group_par, date
from parser.lex_day import print_day

from keyboards.keyboard_creator import create_inline_kb

from lexicon.lexicon import rasp


router = Router()


menu_keyboard = create_inline_kb(2, 'today_pars_button', 'tomorrow_pars_button', 'user_info')

@router.message(Command(commands='menu'))
async def menu(message: Message):
    await message.answer(
        text="ы",
        reply_markup=menu_keyboard
    )