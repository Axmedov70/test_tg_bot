import asyncio
import logging
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from button import makler_narx, telefon_raqam, start_menu, narx, katta_menu, barchasini_tanlang, jihoz_menu, kvartira_menu, maydon, olmazor, tamir_menu, uzoq_muddatga, toshkent_tuman

API_TOKEN = "8427220208:AAGt4drTxPWdYFh8kahn7S5bAh8AL3SWiPc"
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer(f"""
ArzonArendaga xush kelibsiz {message.from_user.full_name}

Kerakli bo‘limni tanlang👇
""", reply_markup = start_menu
)
    

@dp.message(F.text == "Ijaraga beraman")
async def ijaraga_beraman(message: types.Message):
    await message.answer(f"""
Qanday turdagi binoni ijaraga berasiz?

Tugmalardan birini tanlang 👇
""", reply_markup = katta_menu
    )


@dp.message(F.text == "Kvartira")
async def kvartira(message: types.Message):
    await message.answer(f"""
Qancha muddatga ijaraga berasiz?

Tugmalardan birini tanlang 👇
""", reply_markup = kvartira_menu
    )


@dp.message(F.text == "Uzoq muddatga")
async def uzoq_muddatga79(message: types.Message):
    await message.answer(f"""
Qaysi viloyatda joylashgan?
   
Tugmalardan birini tanlang 👇
""", reply_markup = uzoq_muddatga
    )

@dp.message(F.text == "Toshkent")
async def toshkent8(message: types.Message):
    await message.answer(f"""
Qaysi Tumanda?

Tugmalardan birini tanlang 👇
""", reply_markup = toshkent_tuman
    )



@dp.message(F.text == "Olmazor")
async def olmazor1(message: types.Message):
    await message.answer(f"""
Necha xona?

Tugmalardan birini tanlang 👇
""", reply_markup = olmazor
    )


@dp.message(F.text == "3")
async def xona(message: types.Message):
    await message.answer(f"""
Maydoni necha kvadrat bo'lsin? (m²)

Tugmalardan birini tanlang. 👇
""", reply_markup = maydon
    )

@dp.message(F.text == "20m/kv")
async def maydon1(message: types.Message):
    await message.answer(f"""
Ta'miri qanday?

Tugmalardan birini tanlang 👇
""", reply_markup = tamir_menu
    )

@dp.message(F.text == "Yevro ta'mir")
async def maydon2(message: types.Message):
    await message.answer(f"""
Binoda bor qo'shimcha jihozlarni quyidagi tugmalar yordamida tanlang 👇
""", reply_markup = jihoz_menu
    )

@dp.message(F.text == "Barchasini tanlash ✅")
async def maydon3(message: types.Message):
    await message.answer(f"""
📎 Shu belgini bosib rasmlarni yuklang.

Yuklangan 1-rasm asosiy qilib belgilanadi.

❗️Rasm tanlaganigizdan keyin tizim rasmlarni yuklab olish uchun 5-6 soniya kutib turing.️
""", reply_markup = barchasini_tanlang
    )


@dp.message(F.photo)
async def get_photo(message: types.Message):
    await message.answer("""
Agar boshqa rasm bo'lmasa,

Davom etish⏩️ tugmasini bosing.""")


   
    
@dp.message(F.text == "Davom etish⏩️")
async def maydon6(message: types.Message):
    await message.answer(f"""
Narxi qancha? (1 oy uchun)

Tugmalardan birini tanlang 👇
""", reply_markup = narx
    )

@dp.message(F.text == "100$")
async def maydon46(message: types.Message):
    await message.answer(f"""
Makler haqi bormi?

Agar bo'lsa nechi foiz?

Makler haqi yo'q bo'lsa YO'Q tugmasini bosing 👇
""", reply_markup = makler_narx
  )

@dp.message(F.text == "Yo'q")
async def maydon436(message: types.Message):
    await message.answer(f"""
Telefon raqamni yuborish tugmasini bosing,

yoki boshqa raqamingizni shu ko'rinishda yozing!

👉 +998901234567
""", reply_markup = telefon_raqam
    )

@dp.message(F.text == "📱 Telefon raqamni yuborish")
async def maydon43596(message: types.Message):
    await message.answer(f"""
KVARTIRA, UZOQ MUDDATGA
— Manzil: Toshkent, Olmazor
— Ta'miri: Yevro ta'mir
— Necha xona: 3
— Maydoni: 20m/kv
— Narxi: 100$
— Vositachilik haqi: Yo'q
- Jihozlar: Hammasi
Mebel, Televizor, Hammom, Konditsioner, Kir yuvish mashinasi, Mikrotoʻlqinli pech, Muzlatgich, Lift, Avtoturargox, Internet, Telefon tarmogʻi, Sunʻiy yoʻldosh/kabel TV, Videokuzatuv, Gaz taʻminoti, Suv taʻminoti, Kanalizatsiya, Qoʻriqlash, Bolalar maydonchasi
""", reply_markup = telefon_raqam
    )











async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())