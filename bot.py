import asyncio

from aiogram import Bot, Dispatcher, Router
from aiogram.types import BotCommand

from config_data.config import Config, load_config
from handlers import user_handlers
from handlers import update_handlers
from handlers import payment_handlers
from handlers import other_handlers
from handlers import menu_handlers
from handlers import register_handlers
from handlers import edit_handlers


router = Router()


async def main() -> None:
    print("\n\n ---start--- \n")

    config: Config = load_config()

    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()

    main_menu_commands = [
        BotCommand(command='menu',
                   description='Меню'),
        BotCommand(command='/donate',
                   description='на развитие')
    ]

    dp.include_router(register_handlers.router)
    dp.include_router(user_handlers.router)
    dp.include_router(update_handlers.router)
    dp.include_router(payment_handlers.router)
    dp.include_router(menu_handlers.router)
    dp.include_router(edit_handlers.router)


    dp.include_router(other_handlers.router)


    await bot.set_my_commands(main_menu_commands)
    await bot.delete_webhook(drop_pending_updates=False)
    await dp.start_polling(bot, skip_updates=False)


if __name__ == '__main__':
    asyncio.run(main())
