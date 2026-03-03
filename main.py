import asyncio
import logging

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage

from states import arenda_uy
from button import xona, makler_narx, telefon_raqam, start_menu, narx, katta_menu, barchasini_tanlang, jihoz_menu, kvartira_menu, maydon, tamir_menu, uzoq_muddatga, toshkent_tuman
from aiogram.client.session.aiohttp import AiohttpSession

TOKEN = "8427220208:AAGt4drTxPWdYFh8kahn7S5bAh8AL3SWiPc"

# Diqqat: Proxy faqat kerak bo'lsa ishlating, aks holda oddiy session ishlating
PROXY_URL = 'http://proxy.server:3128'
session = AiohttpSession(proxy=PROXY_URL)
bot = Bot(token=TOKEN, session=session)

logging.basicConfig(level=logging.INFO)
dp = Dispatcher(storage=MemoryStorage())

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        f"ArzonArendaga xush kelibsiz {message.from_user.full_name}\n\nKerakli bo‘limni tanlang👇",
        reply_markup=start_menu
    )

@dp.message(F.text == "Ijaraga beraman")
async def ijaraga_berish(message: types.Message, state: FSMContext):
    await message.answer("Qanday turdagi binoni ijaraga berasiz?\n\nTugmalardan birini tanlang 👇", reply_markup=katta_menu)    
    await state.set_state(arenda_uy.kuchmas_mulk)

@dp.message(arenda_uy.kuchmas_mulk)
async def kuchmas_mulk(message: types.Message, state: FSMContext):
    await state.update_data(kuchmas_mulk=message.text)
    await message.answer("Qancha muddatga ijaraga berasiz?\n\nTugmalardan birini tanlang 👇", reply_markup=kvartira_menu)
    await state.set_state(arenda_uy.muddat)

@dp.message(arenda_uy.muddat)
async def muddat(message: types.Message, state: FSMContext):
    await state.update_data(muddat=message.text)
    await message.answer("Qaysi viloyatda joylashgan?\n\nTugmalardan birini tanlang 👇", reply_markup=uzoq_muddatga)
    await state.set_state(arenda_uy.viloyat)

@dp.message(arenda_uy.viloyat)
async def viloyat(message: types.Message, state: FSMContext):
    await state.update_data(viloyat=message.text)
    await message.answer("Qaysi Tumanda?\n\nTugmalardan birini tanlang 👇", reply_markup=toshkent_tuman)
    await state.set_state(arenda_uy.tuman)

@dp.message(arenda_uy.tuman)
async def tuman(message: types.Message, state: FSMContext):
    await state.update_data(tuman=message.text)
    await message.answer("Necha xona?\n\nTugmalardan birini tanlang 👇", reply_markup=xona)
    await state.set_state(arenda_uy.xona)

@dp.message(arenda_uy.xona)
async def xona1(message: types.Message, state: FSMContext):
    await state.update_data(xona=message.text)
    await message.answer("Maydoni necha kvadrat bo'lsin? (m²)\n\nTugmalardan birini tanlang 👇", reply_markup=maydon)
    await state.set_state(arenda_uy.maydon)

@dp.message(arenda_uy.maydon)
async def maydon_step(message: types.Message, state: FSMContext):
    await state.update_data(maydon=message.text)
    await message.answer("Ta'miri qanday?\n\nTugmalardan birini tanlang 👇", reply_markup=tamir_menu)
    await state.set_state(arenda_uy.tamir)

@dp.message(arenda_uy.tamir)
async def tamir(message: types.Message, state: FSMContext):
    await state.update_data(tamir=message.text)
    await message.answer("Binoda bor qo'shimcha jihozlarni quyidagi tugmalar yordamida tanlang 👇", reply_markup=jihoz_menu)
    await state.set_state(arenda_uy.jihozlar)

# "Barchasini tanlang" yoki matn kelganda jihozlarni saqlash
@dp.message(arenda_uy.jihozlar)
async def jihoz(message: types.Message, state: FSMContext):
    await state.update_data(jihozlar=message.text)
    await message.answer("""
📎 Shu belgini bosib rasm yuklang.

Yuklangan rasm asosiy qilib belgilanadi.
""", reply_markup=types.ReplyKeyboardRemove()) # Rasm yuklashda klaviatura xalaqit bermasligi uchun
    await state.set_state(arenda_uy.rasim)

# Faqat rasm yuklanganda ishlaydi
@dp.message(arenda_uy.rasim, F.photo)
async def rasim_step(message: types.Message, state: FSMContext):
    await state.update_data(rasim=message.photo[-1].file_id)
    await message.answer("Narxi qancha? (1 oy uchun)\n\nTugmalardan birini tanlang 👇", reply_markup=narx)
    await state.set_state(arenda_uy.narx)

@dp.message(arenda_uy.narx)
async def narx2(message: types.Message, state: FSMContext):
    await state.update_data(narx=message.text)
    await message.answer("Makler haqi bormi?\n\nAgar bo'lsa nechi foiz?\n\nMakler haqi yo'q bo'lsa YO'Q tugmasini bosing 👇", reply_markup=makler_narx)
    await state.set_state(arenda_uy.makler)

@dp.message(arenda_uy.makler)
async def makler(message: types.Message, state: FSMContext):
    await state.update_data(makler=message.text)
    await message.answer("Telefon raqamni yuborish tugmasini bosing yoki yozing! 👇", reply_markup=telefon_raqam)
    await state.set_state(arenda_uy.tel_raqam)

# Yakuniy natijani chiqarish (Faqat bitta funksiya qoldi)
@dp.message(arenda_uy.tel_raqam)
async def finish_anketa(message: types.Message, state: FSMContext):
    phone = message.contact.phone_number if message.contact else message.text
    await state.update_data(tel_raqam=phone)
    
    data = await state.get_data()

    text = f"""
🌟IJARA-CHI | KVARTIRA

🏦 KUCHMAS MULK: {data.get('kuchmas_mulk')}
⏰ MUDDAT: {data.get('muddat')}
🏔️ VILOYAT: {data.get('viloyat')}
🏙 TUMAN: {data.get('tuman')}
🚪 NECHA XONA: {data.get('xona')}
🏡 MAYDON: {data.get('maydon')}
🛠️ TAMIR: {data.get('tamir')}
🛏️ JIHOZLAR: {data.get('jihozlar')}
💵 NARX: {data.get('narx')}
💳 MAKLER: {data.get('makler')}
📞 TELEFON RAQAM: {data.get('tel_raqam')}

✏️ @{message.from_user.username if message.from_user.username else 'No user'}
"""

    await message.answer_photo(photo=data.get('rasim'), caption=text)
    await message.answer("E'loningiz qabul qilindi!", reply_markup=start_menu)
    await state.clear()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())