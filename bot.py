import datetime
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, Message, BotCommand
from pars_site.all_groups_href import all_groups
from pars_site.parser import group_par, print_day
from Keyboards.LEXICON import create_inline_kb

BOT_TOKEN = '6665715559:AAFi6v6U7gE5Z2USIXd9vk6BTAmvzRnMWp8'
bot = Bot(BOT_TOKEN)
dp = Dispatcher()

keyboard_today = create_inline_kb(1, 'update_button_today')
keyboard_tomorrow = create_inline_kb(1, 'update_button_tomorrow')


async def set_main_menu():
    # Создаем список с командами и их описанием для кнопки menu
    main_menu_commands = [
        BotCommand(command='/today',
                   description='Пары на сегодня'),
        BotCommand(command='/tomorrow',
                   description='Пары на завтра')
    ]

    await bot.set_my_commands(main_menu_commands)


def date(offset_days: int):
    return (datetime.datetime.today() + datetime.timedelta(days=offset_days)).strftime('%d.%m.%Y')


@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=f'привет')


@dp.message(Command(commands='today'))
async def drop_timetable(message: Message):
    today = date(0)
    request_site = group_par('421', 'запрос пар на сегодня', message.from_user.username)
    if today in request_site:
        await message.answer(text=f'<code>{print_day(today, request_site)}</code>',
                             parse_mode='HTML',
                             reply_markup=keyboard_today
                             )
    else:
        await message.answer(f'На сегодня пар уже не будет')


@dp.message(Command(commands='tomorrow'))
async def drop_timetable(message: Message):
    tomorrow = 1
    request_site = group_par('421', 'запрос пар на завтра', message.from_user.username)
    if print_day(date(tomorrow), request_site) != 'единственный выходной 🥳':
        await message.answer(text=f'<code>{print_day(date(tomorrow), request_site)}</code>',
                             parse_mode='HTML',
                             reply_markup=keyboard_tomorrow
                             )
    else:
        await message.answer(f'''Завтра выходной, вот пары на понедельник''')
        await message.answer(text=f'<code>{print_day(date(tomorrow + 1), request_site)}</code>',
                             parse_mode='HTML',
                             reply_markup=keyboard_tomorrow
                             )


@dp.message(Command(commands='week'))
async def drop_timetable(message: Message):
    request_site = group_par()
    for day in request_site:
        await message.answer(text=f'<code>{print_day(day, request_site)}</code>',
                             parse_mode='HTML'
                             )


@dp.callback_query(F.data == 'update_button_today')
async def process_button_1_press(callback: CallbackQuery):
    today = date(0)
    request_site = group_par('421', 'обновление запроса на сегодня', callback.from_user.username)

    try:
        if today in request_site:
            check = print_day(today, request_site)
            if callback.message.text in check:
                await callback.message.edit_text(
                    text=f'<code>{check}</code>',
                    parse_mode='HTML',
                    reply_markup=callback.message.reply_markup
                )
        else:
            await callback.message.edit_text(text=f'На сегодня пар уже не будет')
        await callback.answer(text='Обновлео ✅')

    except Exception:
        await callback.answer(text='Обновлено ✅')


@dp.callback_query(F.data == 'update_button_tomorrow')
async def process_button_1_press(callback: CallbackQuery):
    tomorrow = 1
    request_site = group_par('421', 'обновление запроса на завтра', callback.from_user.username)
    try:
        if print_day(date(tomorrow), request_site) != 'единственный выходной 🥳':
            await callback.message.answer(text=f'<code>{print_day(date(tomorrow), request_site)}</code>',
                                          parse_mode='HTML',
                                          reply_markup=keyboard_tomorrow
                                          )
        else:
            await callback.message.answer(f'''Завтра выходной, вот пары на понедельник''')
            await callback.message.answer(text=f'<code>{print_day(date(tomorrow + 1), request_site)}</code>',
                                          parse_mode='HTML',
                                          reply_markup=keyboard_tomorrow
                                          )

        await callback.answer(text='Обновлено ✅')
    except Exception:
        await callback.answer(text='Обновлено ✅')


if __name__ == '__main__':
    dp.startup.register(set_main_menu)
    dp.run_polling(bot)
