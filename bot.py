import asyncio

from aiogram import Bot, Dispatcher, Router
from aiogram.types import BotCommand

from config_data.config import Config, load_config
from handlers import user_handlers, update_handlers


router = Router()


async def main() -> None:

    config: Config = load_config()

    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()

    main_menu_commands = [
        BotCommand(command='/today',
                   description='Пары на сегодня'),
        BotCommand(command='/tomorrow',
                   description='Пары на завтра'),
        BotCommand(command='/donate',
                   description='чисто на карман накинуть хочу')
    ]

    dp.include_router(user_handlers.router)
    dp.include_router(update_handlers.router)

    await bot.set_my_commands(main_menu_commands)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
