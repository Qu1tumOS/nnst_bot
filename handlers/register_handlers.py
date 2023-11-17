from aiogram import Router, F
from aiogram.types import CallbackQuery

from parser.href_groups import groups

from keyboards.keyboard_creator import create_inline_kb

from DB.db_connect import *


router = Router()

registered = create_inline_kb(1, 'menu_button')
not_registered = create_inline_kb(2, 'NNST', 'NAMT')
groups_all = create_inline_kb(6, **groups)
profile = create_inline_kb(1, 'user_info')

@router.callback_query(F.data == 'log_button')
async def process_button_2_press(callback: CallbackQuery):
    user_info = session.query(User).filter(User.tg_id==callback.from_user.id).first()

    if user_info == None:
        session.add(User(tg_id=callback.from_user.id,
                         name=callback.from_user.username))
        session.commit()
        await callback.message.edit_text(
        text=f'''Окей, тебя нет в нашей базе, пройди небольшую регистрацию\n\nВыбери свой техникум:''',
        reply_markup=not_registered
    )

    else:
        await callback.message.edit_text(
        text=f'''ты уже зареган''',
        reply_markup=registered
    )
    await callback.answer()

@router.callback_query(F.data == 'NNST')
async def process_button_2_press(callback: CallbackQuery):
    user_info = session.query(User).filter(User.tg_id==callback.from_user.id).first()
    user_info.collage == 'ННСТ'
    await callback.message.edit_text(text='Теперь выбери свою группу',
                                     reply_markup=groups_all)

@router.callback_query(F.data == 'NAMT')
async def process_button_2_press(callback: CallbackQuery):
    await callback.message.edit_text(text='Извини, для этого техникума расписание пока не готово :(',
                                     reply_markup=profile)

@router.callback_query(F.data.in_(groups))
async def process_button_2_press(callback: CallbackQuery):
    user = session.query(User).filter(User.tg_id==callback.from_user.id).first()
    user.group == callback.data
    await callback.answer()