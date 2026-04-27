from aiogram.fsm.state import StatesGroup, State

class FoodChoice(StatesGroup):
    waiting_for_food_name = State() # Шаг, где мы ждем название блюда