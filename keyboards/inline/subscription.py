from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

check_button = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardMarkup(text="Obunani tekshirish",callback_data="check_subs")
    ]]
)