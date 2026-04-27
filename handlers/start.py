from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from states.food_states import FoodChoice

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message, state: FSMContext):
    await message.answer("Привет! Какая еда тебе нравится?")
    await state.set_state(FoodChoice.waiting_for_food_name)