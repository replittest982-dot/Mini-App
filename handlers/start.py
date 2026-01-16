from aiogram import Router, types
from aiogram.filters import CommandStart
from keyboards.inline import get_webapp_keyboard

router = Router()

@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(
        "Привет! Нажми на кнопку ниже, чтобы запустить приложение:",
        reply_markup=get_webapp_keyboard()
    )
