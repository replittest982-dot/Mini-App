from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from config import WEBAPP_URL

router = Router()

@router.message(CommandStart())
async def cmd_start(message: types.Message):
    # Создаем кнопку с твоей ссылкой
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="🎮 Играть в Крестики-Нолики", 
            web_app=WebAppInfo(url=WEBAPP_URL)
        )]
    ])
    
    await message.answer(
        f"Привет, {message.from_user.first_name}!\n"
        "Я бот с искусственным интеллектом.\n"
        "Жми кнопку, чтобы попробовать меня обыграть! 👇",
        reply_markup=markup
    )
