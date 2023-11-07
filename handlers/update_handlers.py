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
    week_pars = group_par('421',
                             'обновление запроса на сегодня',
                             callback.from_user.username)

    try:
        if today in week_pars:
            check = print_day(today, week_pars)
            if callback.message.text not in check:
                await callback.message.edit_text(
                    text=f'`{check}`',
                    parse_mode='MarkdownV2',
                    reply_markup=callback.message.reply_markup
                )
            else:
                await callback.answer(text='Обновлено ✅')
        else:
            await callback.message.edit_text('Сегодня пар уже не будет')
        await callback.answer(text='Обновлено ✅')

    except Exception as x:
        print(f'ошибка в выводе пар на сегодня :{x}')


@router.callback_query(F.data == 'update_button_tomorrow')
async def process_button_2_press(callback: CallbackQuery):
    tomorrow = 1
    request_site = group_par('421',
                             'обновление запроса на завтра',
                             callback.from_user.username)
    try:
        if print_day(date(tomorrow), request_site) != 'единственный выходной 🥳':
            await callback.message.edit_text(
                text=f'`{print_day(date(tomorrow), request_site)}`',
                parse_mode='MarkdownV2',
                reply_markup=keyboard_tomorrow
            )
        else:
            await callback.message.edit_text(
                text=f'`{print_day(date(tomorrow + 1), request_site)}`',
                parse_mode='MarkdownV2',
                reply_markup=keyboard_tomorrow
            )

        await callback.answer(text='Обновлено ✅')
    except Exception:
        await callback.answer(text='Обновлено ✅')
