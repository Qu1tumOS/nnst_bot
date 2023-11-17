from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


LEXICON: dict[str, str] = {
    'update_button_today': 'Обновить',
    'update_button_tomorrow': 'Обновить',
    'menu_button': 'Меню',
    'next_day_par': 'Пары завтра',
    'log_button': 'Вход',
    'today_pars_button': 'Сегодня',
    'tomorrow_pars_button': 'Завтра',
    'user_info': 'Профиль',
    'edit_user_info': 'Редактировать',

    'pn_button': 'Пн',
    'vt_button': 'Вт',
    'sr_button': 'Ср',
    'cht_button': 'Чт',
    'pt_button': 'Пт',
    'sb_button': 'СБ',

    'week_buttons': 'На неделю',
    'NST': 'НСТ',
    'NAMT': 'НАМТ',
    '1_subgroup': '1',
    '2_subgroup': '2',

    'edit_collage': 'Техникум',
    'edit_group': 'Группу',
    'edit_subgroup': 'Подгруппу',
    'back_profile': '<- Вернуться',
    'back_edit': '<- Вернуться'

    }

BUTTONS: dict[str, str] = {
    'btn_1': '1',
    'btn_2': '2',
    'btn_3': '3',
    'btn_4': '4',
    'btn_5': '5',
    'btn_6': '6',
    'btn_7': '7',
    'btn_8': '8',
    'btn_9': '9',
    'btn_10': '10',
    'btn_11': '11'}


def create_inline_kb(width: int,
                     *args: str,
                     **kwargs: str) -> InlineKeyboardMarkup:
    # Инициализируем билдер
    kb_builder = InlineKeyboardBuilder()
    # Инициализируем список для кнопок
    buttons: list[InlineKeyboardButton] = []

    # Заполняем список кнопками из аргументов args и kwargs
    if args:
        for button in args:
            buttons.append(InlineKeyboardButton(
                text=LEXICON[button] if button in LEXICON else button,
                callback_data=button))
    if kwargs:
        for button, text in kwargs.items():
            buttons.append(InlineKeyboardButton(
                text=text,
                callback_data=button))

    # Распаковываем список с кнопками в билдер методом row c параметром width
    kb_builder.row(*buttons, width=width)

    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()
