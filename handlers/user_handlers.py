from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from parser.parser import group_par, date
from parser.lex_day import print_day

from keyboards.keyboard_creator import create_inline_kb

from lexicon.lexicon import rasp


router = Router()

keyboard_menu = create_inline_kb(1, 'log_button')


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text="Войди в аккаунт или пройди небольшую регистрацию",
        reply_markup=keyboard_menu
        )


