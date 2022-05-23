from aiogram.types import Message
from loader import dp
from keyboards.inline.aboutBot import categoryAboutBot


#-------------------------------This bot information----------------------------------
@dp.message_handler(text_contains='Bot haqida')
async def send_link(message: Message):
    await message.answer("Bosh dasturlovchi:<b>Timur Karabayev</b>\n"
                         "Testr: <b>Begzod  </b>\n"
                         "G'oya muallifi <b>Azamatjon</b>\n"
                         "Biz bilan aloqa: <b>+998 (99) 040-40-47</b>\n"
                         "Bizning Jamoa: <b>BLACK CODERS</b>\n",reply_markup=categoryAboutBot )

#------------------//--------------This bot information----------------//------------------