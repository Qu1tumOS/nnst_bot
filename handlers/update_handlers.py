from aiogram import Router, F
from aiogram.types import CallbackQuery

from parser.parser import group_par, date
from parser.lex_day import print_day
from keyboards.keyboard_creator import create_inline_kb


router = Router()

keyboard_today = create_inline_kb(1, 'update_button_today')
keyboard_tomorrow = create_inline_kb(1, 'update_button_tomorrow')


@router.callback_query(F.data == 'update_button_today')
async def process_button_1_press(callback: CallbackQuery):
    today = date(0)
    request_site = group_par('421',
                             'обновление запроса на сегодня',
                             callback.from_user.username)

    try:
        if today in request_site:
            check = print_day(today, request_site)
            if callback.message.text in check:
                await callback.message.edit_text(
                    text=f'`{check}`',
                    parse_mode='MarkdownV2',
                    reply_markup=callback.message.reply_markup
                )
        else:
            await callback.message.edit_text('На сегодня пар уже не будет')
        await callback.answer(text='Обновлео ✅')

    except Exception:
        await callback.answer(text='Обновлено ✅')


@router.callback_query(F.data == 'update_button_tomorrow')
async def process_button_2_press(callback: CallbackQuery):
    tomorrow = 1
    request_site = group_par('421',
                             'обновление запроса на завтра',
                             callback.from_user.username)
    try:
        if print_day(date(tomorrow), request_site) != 'единственный выходной 🥳':
            await callback.message.edit_text(f'`{print_day(date(tomorrow), request_site)}`',
                                             parse_mode='MarkdownV2',
                                             reply_markup=keyboard_tomorrow
                                             )
        else:
            await callback.message.edit_text(f'`{print_day(date(tomorrow + 1), request_site)}`',
                                             parse_mode='MarkdownV2',
                                             reply_markup=keyboard_tomorrow
                                             )

        await callback.answer(text='Обновлено ✅')
    except Exception:
        await callback.answer(text='Обновлено ✅')
