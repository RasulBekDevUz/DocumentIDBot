import sys
import os
import time
words = """\033[1;33mCoded \033[1;31mBy \033[1;32mRasul \033[1;36mTelegram \033[1;34m>>>  \033[1;35m@KgzNet"""
for char in words:
	 time.sleep(0.05)
	 sys.stdout.write(char)
	 sys.stdout.flush()
time.sleep(1.7)
os.system("clear")	 
print("\033[1;32m")
from aiogram import Bot,Dispatcher,types,executor
TOKEN="6243017204:AAFspkSm_9XKIXxUrk2w2dXCQb_EKxHguCU"
api_id = 10953300
api_hash = "9c24426e5d6fa1d441913e3906627f87"
admins=[1578385827]
token=TOKEN
bot=Bot(token) 
dp=Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(f"<a href='tg://user?id={message.from_id}'>AsalomuAleykum👋🏻</a> Bu  bot 🤖 orqali file larni id Raqami orqali ola olasiz qila olasiz✅ Foydalanish uchun : Id olmoqchi bosez file jonating >>file ni olmoqchi bosez botga id ni tashlang", parse_mode="HTML")

@dp.message_handler(content_types=['text'])
async def decode(msg:types.Message):
    try:
        await msg.answer_document(document=f'{msg.text}')
    except:await msg.answer("Bu ID Kodi boyicha hechqanday malumot topilmadi 🤨🧐😡 ")
@dp.message_handler(content_types=[types.ContentType.DOCUMENT,types.ContentType.AUDIO,types.ContentType.ANIMATION,types.ContentType.VOICE,types.ContentType.VIDEO,types.ContentType.PHOTO]  )
async def decode(msg:types.Message):
    z=msg.document.file_id or msg.animation.file_id or msg.audio.file_id or msg.voice.file_id 
    await msg.answer(f'{z}')
    

if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True)
