from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from loader import dp,bot
from aiogram.types import CallbackQuery
from data.config import ADMINS,CHANELLS
from aiogram.dispatcher import FSMContext
from states.personalData import PersonalData
from keyboards.default.anketaFull import post_callback
from keyboards.inline.manage_post import confirmation_keyboard



#------------------------states to register------------------------------

PHONE_NUM = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'


@dp.message_handler(text_contains='Murojat yuborish', state=None)
async def enter_test(message: types.Message):
    await message.answer("To'liq ism va familiyangizni kiriting:\n"
                         "<b>Misol:(Timur Karabayev)</b>")
    await PersonalData.fullname.set()


@dp.message_handler(state=PersonalData.fullname)
async def answer_fullname(message: types.Message, state: FSMContext):
    fullname = message.text
    await state.update_data(
        {"name": fullname}
    )
    await state.update_data(text=message.html_text, mention=message.from_user.get_mention())
    await message.answer("📞<b>Aloq:</b>\n\nBog'lanish uchun raqamingizni kiriting!:\n"
                         "Misol:(+998 99 123 45 67)")

    await PersonalData.next()


@dp.message_handler(state=PersonalData.phone)
async def answer_phone(message: types.Message, state: FSMContext):
    phone = message.text
    await state.update_data(
        {"phone":phone}
    )



    await state.update_data(text=message.html_text, mention=message.from_user.get_mention())
    await message.answer("🏢 <b>Fakultet:</b>\n\n"
                         "Misol:(22EE21)")
    await PersonalData.next()


@dp.message_handler(state=PersonalData.course_name)
async def answer_course_name(message: types.Message, state: FSMContext):
    course_name = message.text

    await state.update_data(
        {"course_name":course_name}
    )
    await state.update_data(text=message.html_text, mention=message.from_user.get_mention())
    await message.answer("🗣 <b>Murojatchingiz</b>\n\n"
                         "Misol:(Dekan) ")
    await PersonalData.next()


@dp.message_handler(state=PersonalData.murojat_kimga)
async def answer_murojat_kimga(message: types.Message, state: FSMContext):
    murojat_kimga = message.text
    await state.update_data(
        {"murojat_kimga": murojat_kimga}
    )
    await state.update_data(text=message.html_text, mention=message.from_user.get_mention())
    await message.answer("📑 <b>Murojat</b>\n\n"
                         "Iltimos murojatingizni to'liq yozing!")
    await PersonalData.next()


@dp.message_handler(state=PersonalData.murojat)
async def answer_murojat(message: types.Message, state: FSMContext):
    murojat = message.text
    await state.update_data(
        {"murojat": murojat}
    )
    await PersonalData.next()
# ----------//--------------states to register------------//------------------



#-----------------------show back to user data-----------------------

    malumotlar_chiq = await state.get_data()
    name = malumotlar_chiq.get("name")
    course_name = malumotlar_chiq.get("course_name")
    phone = malumotlar_chiq.get("phone")
    murojat_kimga = malumotlar_chiq.get("murojat_kimga")
    murojat = malumotlar_chiq.get("murojat")

    msg = "<b>Quyidai ma`lumotlar qabul qilindi:</b>\n\n"
    msg += f"👨‍ Ism va Familiyangiz: - <b>{name.title()}</b>\n"
    msg += f"🏤 Fakultet:  - <b>{course_name.upper()}</b>\n"
    msg += f"📞 Telefon: - <b>{phone}</b>\n"
    msg += f"🇺🇿 Telegram: @{message.from_user.username}\n "
    msg += f"🗣 Murojat kimga: - <b>{murojat_kimga.title()}</b>\n"
    msg += f"📝 Murojatingiz: - <b>{murojat}</b>\n\n\n"
    msg += f"👉 @timurPythonDev\n"
    msg += f"👉 @BlackCodersTeamOfficial\n"
    msg += f"👉 @palitexnikainsitut"

# ----------//-------------show back to user data and user data---------//--------------

    await message.answer(msg)
    await message.answer("Murojatingizni to'g'ri bo'lsa\n<b>Tasdiqlash</b> tugmasini bosin?", reply_markup=confirmation_keyboard)
    await state.update_data(text=msg, mention=message.from_user.get_mention())
    await PersonalData.next()

#-------------------------send user data to the admin----------------------

@dp.callback_query_handler(post_callback.filter(action="post"), state=PersonalData.Confirm)
async def confirm_post(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        text = data.get('text')
        mention = data.get('mention')
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("Sizning arizangiz qabul qilindi 12  yoki 24 soatda ko'rib chiqiladi")
    await bot.send_message(ADMINS[0], f"Foydalanuvchi {mention} quyidagi murojatni yubordi")
    await bot.send_message(ADMINS[0], text, parse_mode="HTML",reply_markup=confirmation_keyboard)

@dp.callback_query_handler(post_callback.filter(action="cancel"), state=PersonalData.Confirm)
async def cancel_post(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("❌ Sizning murojatingiz rad etildi.")


@dp.message_handler(state=PersonalData.Confirm)
async def post_unknown(message: types.Message):
    await message.answer("Iltimos murojatingizni jonatin yoki rad eting!!")

@dp.callback_query_handler(post_callback.filter(action="post"), user_id=ADMINS)
async def approve_post(call: CallbackQuery):
    await call.answer("Murojatni yuborishga ruhsat berdingiz.", show_alert=True)
    target_channel = CHANELLS[2]
    message = await call.message.edit_reply_markup()
    await message.send_copy(chat_id=target_channel)

@dp.callback_query_handler(post_callback.filter(action="cancel"), user_id=ADMINS)
async def decline_post(call: CallbackQuery):
    await call.answer("❌ Murojat rad etildi.", show_alert=True)
    await call.message.edit_reply_markup()

#-------------//------------send user data to the admin-----------//-------------