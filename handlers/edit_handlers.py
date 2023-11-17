from aiogram import Router, F
from aiogram.types import CallbackQuery

from parser.href_groups import groups

from keyboards.keyboard_creator import create_inline_kb

from DB.db_connect import *


router = Router()

edit_keyboard = create_inline_kb(1, 'edit_group', 'edit_subgroup', 'back_profile')
back_keyboard = create_inline_kb(2, 'menu_button', 'user_info')
user_info_keyboard = create_inline_kb(2, 'menu_button', 'edit_user_info')
subgroup_keyboard = create_inline_kb(2, '1_subgroup', '2_subgroup', 'back_edit')
groups_all = create_inline_kb(6, **groups)



@router.callback_query(F.data == 'edit_user_info')
async def process_button_2_press(callback: CallbackQuery):
    await callback.message.edit_text(
        text='Что нужно изменить?',
        reply_markup=edit_keyboard
    )

@router.callback_query(F.data == 'edit_collage')
async def process_button_2_press(callback: CallbackQuery):
    await callback.message.edit_text(
        text='Техникум пока, что изменить нельзя :(',
        reply_markup=back_keyboard
    )

@router.callback_query(F.data == 'edit_group')
async def process_button_2_press(callback: CallbackQuery):
    await callback.message.edit_text(
        text='Выбери новую группу',
        reply_markup=groups_all
    )

@router.callback_query(F.data == 'edit_subgroup')
async def process_button_2_press(callback: CallbackQuery):
    await callback.message.edit_text(
        text='выбери нужную подгруппу',
        reply_markup=subgroup_keyboard
    )

@router.callback_query(F.data == 'back_profile')
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

@router.callback_query(F.data == 'back_edit')
async def process_button_2_press(callback: CallbackQuery):
    await callback.message.edit_text(
        text='Что нужно изменить?',
        reply_markup=edit_keyboard
    )
