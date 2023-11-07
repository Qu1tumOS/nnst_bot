from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from parser.parser import group_par, date
from parser.lex_day import print_day

from keyboards.keyboard_creator import create_inline_kb


router = Router()

keyboard_today = create_inline_kb(1, 'update_button_today')
keyboard_tomorrow = create_inline_kb(1, 'update_button_tomorrow')


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text="привет"
        )


@router.message(Command(commands='today'))
async def drop_timetable_today(message: Message):
    today = date(0)
    request_site = group_par('421',
                             'запрос пар на сегодня',
                             message.from_user.username)
    if today in request_site:
        await message.answer(
            text=f'`{print_day(today, request_site)}`',
            parse_mode='MarkdownV2',
            reply_markup=keyboard_today
        )
    else:
        await message.answer('На сегодня пар уже не будет')


@router.message(Command(commands='tomorrow'))
async def drop_timetable_tomorrow(message: Message):
    tomorrow = 1
    next_tmrw = 2
    request_site = group_par('421',
                             'запрос пар на завтра',
                             message.from_user.username)
    if print_day(date(tomorrow), request_site) != 'единственный выходной 🥳':
        await message.answer(
            text=f'`{print_day(date(tomorrow), request_site)}`',
            parse_mode='MarkdownV2',
            reply_markup=keyboard_tomorrow
        )
    else:
        await message.answer('''Завтра выходной, вот пары на понедельник''')
        await message.answer(
            text=f'`{print_day(date(next_tmrw), request_site)}`',
            parse_mode='MarkdownV2',
            reply_markup=keyboard_tomorrow
        )
