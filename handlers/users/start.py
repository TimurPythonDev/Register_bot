import sqlite3

from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from loader import bot,dp,db
from data.config import CHANELLS, ADMINS
from utils.misc import subscriber
from keyboards.default.menu import menu
from keyboards.inline.subscription import check_button


@dp.message_handler(commands=['users'])
async def bot_start(message: types.Message):
    pass
    # name = message.from_user.full_name
    # Foydalanuvchini bazaga qo'shamiz
    # try:
    #     db.add_user(id=message.from_user.id,
    #                 name=name)
    # except sqlite3.IntegrityError as err:
    #     await bot.send_message(chat_id=ADMINS[0], text=err)

    # count = db.count_users()[0]
    # msg = f"Foydalanuvchilar soni\nBazada {count} ta foydalanuvchi bor."
    # await bot.send_message(chat_id=ADMINS[0])

#-------------------------This it checks the subscriber--------------------------------

@dp.message_handler(commands=['start'])
async def show_channels(message: types.Message):
    name = message.from_user.full_name
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
    except sqlite3.IntegrityError as err:
        pass
    #     await bot.send_message(chat_id=ADMINS[0], text=err)
    # await bot.send_message(chat_id=ADMINS[0])
    channels_format = str()
    for channel in CHANELLS:
        chat = await bot.get_chat(channel)
        invite_link = await chat.export_invite_link()
        channels_format += f"👉 <a href='{invite_link}'>{chat.title}</a>\n"

    await message.answer(f"Quyidagi kanallarga obuna bo'ling: \n"
                         f"{channels_format}",
                         reply_markup=check_button,
                         disable_web_page_preview=True)

@dp.callback_query_handler(text="check_subs")
async def checker(call: types.CallbackQuery):
    await call.answer()
    result = str()
    for channel in CHANELLS:
        status = await subscriber.check(user_id=call.from_user.id,
                                          channel=channel)
        channel = await bot.get_chat(channel)
        if status:
            result += f"✅ <b>{channel.title}</b> kanaliga obuna bo'lgansiz!\n\n"
        else:
            invite_link = await channel.export_invite_link()
            result += (f"❌ <b>{channel.title}</b> kanaliga obuna bo'lmagansiz. "
                       f"<a href='{invite_link}'>Obuna bo'ling</a>\n\n")

    await call.message.answer(result, disable_web_page_preview=True,reply_markup=menu)

#--------------//-------------This it checks the subscriber------------------//---------------
