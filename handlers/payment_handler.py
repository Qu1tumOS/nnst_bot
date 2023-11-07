from aiogram import Router, Bot
from aiogram.filters import Command
from aiogram.types import Message, InputFile

from keyboards.payment_keyboard import Pay_keyboard


router = Router()

@router.message(Command(commands='donate'))
async def donate(message: Message):
    await message.answer(
        text='на аренду сервера',
        reply_markup=Pay_keyboard
    )
