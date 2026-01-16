from aiogram import Router, F, types

router = Router()

@router.message(F.web_app_data)
async def handle_webapp_data(message: types.Message):
    data = message.web_app_data.data
    await message.answer(f"📦 Получены данные из Mini App: {data}")
