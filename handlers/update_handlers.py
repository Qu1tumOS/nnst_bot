from aiogram import Router, F
from aiogram.types import CallbackQuery

from parser.parser import group_par, date
from parser.lex_day import print_day

from keyboards.keyboard_creator import create_inline_kb

from DB.db_connect import *


router = Router()

keyboard_today = create_inline_kb(2, 'menu_button', 'update_button_today')
keyboard_tomorrow = create_inline_kb(2, 'menu_button', 'update_button_tomorrow')
keyboard_not_today = create_inline_kb(2, 'menu_button', 'next_day_par')
week_keyboard = create_inline_kb(6, 'pn_button', 'vt_button', 'sr_button', 'cht_button', 'pt_button', 'sb_button', 'menu_button')
user_info_keyboard = create_inline_kb(2, 'menu_button', 'edit_user_info')


@router.callback_query(F.data == 'today_pars_button')
async def process_button_1_press(callback: CallbackQuery):
    user = session.query(User).filter(User.tg_id==callback.from_user.id).first()

    today = date(0)
    week_pars = group_par(user.group)

    if today in week_pars:
        check = print_day(today, week_pars, user.subgroup)
        if callback.message.text not in check:
            await callback.message.edit_text(
                text=f'`{check}`',
                parse_mode='MarkdownV2',
                reply_markup=keyboard_today
            )
    else:
        await callback.message.edit_text(text='Сегодня пар уже не будет',
                                         reply_markup=keyboard_not_today)


@router.callback_query(F.data == 'tomorrow_pars_button')
async def process_button_1_press(callback: CallbackQuery):
    user = session.query(User).filter(User.tg_id==callback.from_user.id).first()

    tomorrow = 1
    next_tmrw = 2
    request_site = group_par(user.group)
    if print_day(date(tomorrow), request_site, user.subgroup) != 'единственный выходной 🥳':
        await callback.message.edit_text(
            text=f'`{print_day(date(tomorrow), request_site, user.subgroup)}`',
            parse_mode='MarkdownV2',
            reply_markup=keyboard_tomorrow
        )
    else:
        await callback.message.edit_text('''Завтра выходной, вот пары на понедельник''')
        await callback.message.edit_text(
            text=f'`{print_day(date(next_tmrw), request_site, user.subgroup)}`',
            parse_mode='MarkdownV2',
            reply_markup=keyboard_tomorrow
        )


@router.callback_query(F.data == 'update_button_today')
async def process_button_1_press(callback: CallbackQuery):
    user = session.query(User).filter(User.tg_id==callback.from_user.id).first()

    today = date(0)
    week_pars = group_par(user.group)

    if today in week_pars:
        check = print_day(today, week_pars, user.subgroup)
        if callback.message.text not in check:
            await callback.message.edit_text(
                text=f'`{check}`',
                parse_mode='MarkdownV2',
                reply_markup=callback.message.reply_markup
            )
        else:
            await callback.answer(text='Расписание не изменилось ✅')
    else:
        await callback.message.edit_text(text='Сегодня пар уже не будет',
                                            reply_markup=keyboard_tomorrow)
    await callback.answer(text='Обновлено ✅')


@router.callback_query(F.data == 'update_button_tomorrow')
async def process_button_2_press(callback: CallbackQuery):
    user = session.query(User).filter(User.tg_id==callback.from_user.id).first()
    request_site = group_par(user.group)

    tomorrow = 1
    check = print_day(date(tomorrow), request_site, user.subgroup)
    if print_day(date(tomorrow), request_site, user.subgroup) != 'единственный выходной 🥳':
        if callback.message.text not in check:
            await callback.message.edit_text(
                text=f'`{print_day(date(tomorrow), request_site, user.subgroup)}`',
                parse_mode='MarkdownV2',
                reply_markup=keyboard_tomorrow
            )
        else:
            await callback.answer(text='Расписание не изменилось ✅')
    else:
        checkk = print_day(date(tomorrow + 1), request_site, user.subgroup)
        if callback.message.text not in checkk:
            await callback.message.edit_text(
                text=f'`{checkk}`',
                parse_mode='MarkdownV2',
                reply_markup=keyboard_tomorrow
            )
        else:
            await callback.answer(text='Расписание не изменилось ✅')
    await callback.answer(text='Обновлено ✅')


@router.callback_query(F.data == 'next_day_par')
async def process_button_2_press(callback: CallbackQuery):
    user = session.query(User).filter(User.tg_id==callback.from_user.id).first()

    today_next = date(1)
    request_site = group_par(user.group)
    await callback.message.edit_text(
        text=f'`{print_day(today_next, request_site, user.subgroup)}`',
        parse_mode='MarkdownV2',
        reply_markup=keyboard_tomorrow
    )


@router.callback_query(F.data == 'week_buttons')
async def process_button_2_press(callback: CallbackQuery):
    await callback.message.edit_text(
        text='На какой день недели нужно расписание?',
        reply_markup=week_keyboard
    )


@router.callback_query(F.data == 'user_info')
async def process_button_2_press(callback: CallbackQuery):
    user = session.query(User).filter(User.tg_id==callback.from_user.id).first()
    await callback.message.edit_text(
        text=
f'Имя аккаунта: @{user.name}\n\
Техникум: {user.collage}\n\
Группа: {user.group}\n\
Подгруппа: {user.subgroup}',
        reply_markup=user_info_keyboard
    )