from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📝 Murojat yuborish"),
        ],
        [
            KeyboardButton(text=" 🤖 Bot haqida")
        ],
    ],
    resize_keyboard=True
)