import  logging
from loader import bot
from aiogram import types
from data.config import CHANELLS
from utils.misc import subscriber
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware




#----------------------respond here without sending user data to the handler---------------------

class BigBrother(BaseMiddleware):
    async def on_pre_process_update(self,update:types.Update,data:dict):
        if update.message:
            user = update.message.from_user.id
            if update.message.text in ['/start', '/help']:
                return
        elif update.callback_query:
            user = update.callback_query.from_user.id
            if update.callback_query.data == "check_subs":
                return
        else:
            return
        logging.info(user)
        result = "Botdan foydalanish uchun quyidagi kanallarga obuna bo'ling:\n"
        final_status = True
        for channel in CHANELLS:
            status = await subscriber.check(user_id=user,
                                            channel=channel)
            final_status *= status
            channel = await bot.get_chat(channel)
            if not status:
                invite_link = await channel.export_invite_link()
                result += (f"👉 <a href='{invite_link}'>{channel.title}</a>\n"
                           f"Kannalarga obuna bo'lib qaytadan /start bosin")

        if not final_status:
            await update.message.answer(result, disable_web_page_preview=True)
            raise CancelHandler()

#----------//------------respond here without sending user data to the handler----------//-----------