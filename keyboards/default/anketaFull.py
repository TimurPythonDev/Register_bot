from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from aiogram.utils.callback_data import CallbackData


post_callback = CallbackData("create_post","action")

anketaFull1 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="HA"),
        ],
        [
            KeyboardButton(text="YO'Q"),
        ],
    ],
    resize_keyboard=True
)