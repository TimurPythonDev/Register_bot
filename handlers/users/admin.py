import asyncio
from aiogram import types
from loader import dp, db, bot
from data.config import ADMINS
from keyboards.inline.rekTimur import rek_tim


@dp.message_handler(text="/allusers", user_id=ADMINS)
async def get_all_users(message: types.Message):
    count_users = db.count_users()
    all_users = db.select_all_users()
    # msg = f"Ism: {all_users}"
    msg = f"Foydalanuvchilar soni: <b>{count_users}</b>"

    await message.answer(msg)

@dp.message_handler(text="/timurrek", user_id=ADMINS)
async def send_ad_to_all(message: types.Message):
    users = db.select_all_users()
    for user in users:
        user_id = user[0]
        await bot.send_message(chat_id=user_id, text="<b><i>Assalomu alaykum Hurmatli obunachilar!!\n"
                                                     "Bizno ishtimoyi tarmoqlarda doimo kuzatib borin</i></b>",reply_markup=rek_tim)
        await asyncio.sleep(0.05)

@dp.message_handler(text="/cleandb", user_id=ADMINS)
async def get_all_users(message: types.Message):
    db.delete_users()
    await message.answer("Baza tozalandi!")