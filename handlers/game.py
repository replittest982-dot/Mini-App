from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from config import WEBAPP_URL # Импортируем ссылку

router = Router()

# 1. Команда /game для запуска
@router.message(Command("game"))
async def cmd_game(message: types.Message):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="🎮 Начать битву (AI)", 
            web_app=WebAppInfo(url=WEBAPP_URL)
        )]
    ])
    await message.answer(
        "<b>Крестики-Нолики vs Искусственный Интеллект</b>\n"
        "Жми кнопку, чтобы доказать превосходство человечества! 👇",
        reply_markup=markup,
        parse_mode="HTML"
    )

# 2. Обработка результата (когда игра закончилась)
@router.message(F.web_app_data)
async def process_game_result(message: types.Message):
    result = message.web_app_data.data # Получаем "win", "loss" или "draw"
    
    if result == 'win':
        text = "🎉 <b>ПОБЕДА!</b> Ты уничтожил алгоритм!"
    elif result == 'loss':
        text = "💀 <b>ПОРАЖЕНИЕ...</b> Скайнет победил."
    elif result == 'draw':
        text = "🤝 <b>НИЧЬЯ.</b> Силы равны."
    else:
        text = f"Получены данные: {result}"

    await message.answer(text, parse_mode="HTML")
