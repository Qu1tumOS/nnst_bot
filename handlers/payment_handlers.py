from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from keyboards.payment_keyboard import Pay_keyboard


router = Router()

@router.message(Command(commands='donate'))
async def donate(message: Message):
    await message.answer(
        text='Это для аренды сервера (💵)',
        reply_markup=Pay_keyboard
    )
