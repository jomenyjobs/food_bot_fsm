from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from states import FoodChoice

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message, state: FSMContext):
    await message.answer("Привет! Какая еда тебе нравится?")
    await state.set_state(FoodChoice.waiting_for_food_name)

@router.message(FoodChoice.waiting_for_food_name)
async def food_chosen(message: types.Message, state: FSMContext):
    answer = message.text.lower()
    
    if "бургер" in answer:
        await message.answer("Хммм, бургер — отличная еда! 🍔")
    elif "спагети" in answer or "спагетти" in answer:
        await message.answer("Хммм, мне не нравятся спагети, но все же это хорошее блюдо. 🍝")
    else:
        await message.answer(f"О, {message.text}? Интересный выбор!")
    
    await state.clear() # Завершаем цепочку