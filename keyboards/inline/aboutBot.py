from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup



categoryAboutBot = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔗 Youtubega o'tish",url='https://www.youtube.com/channel/UCiaOKUvfq0TUVSaZIlAcG0A'),
        ],
        [
            InlineKeyboardButton(text="🔗 BLACK CODERS sahifasiga o'tish",url='www.blackcoders.uz'),
        ],
        [
            InlineKeyboardButton(text="🔍 Qidirish", switch_inline_query_current_chat=""),
        ],
        [
            InlineKeyboardButton(text="✉️  Ulashish", switch_inline_query="Assalomu alekum!\nNamangan Palitexnika instituti murojat bo'ti"),
        ]
    ]
)