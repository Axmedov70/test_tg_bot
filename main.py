import asyncio
import logging

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage

from states import arenda_uy
from button import xona_menu, makler_narx, telefon_raqam, start_menu, narx, katta_menu, barchasini_tanlang, jihoz_menu, muddat_menu, maydon_menu, tamir_menu, viloyat_menu, toshkent_tuman

TOKEN = "8427220208:AAGt4drTxPWdYFh8kahn7S5bAh8AL3SWiPc"

bot = Bot(token=TOKEN)
logging.basicConfig(level=logging.INFO)

dp = Dispatcher(storage=MemoryStorage())


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
    f"""
ArzonArendaga xush kelibsiz {message.from_user.full_name}

Kerakli bo‘limni tanlang👇
""",
        reply_markup=start_menu
)


@dp.message(F.text == "Ijaraga beraman")
async def ijaraga_berish(message: types.Message, state: FSMContext):
    await message.answer(f"""
Qanday turdagi binoni ijaraga berasiz?

Tugmalardan birini tanlang 👇
""", reply_markup=katta_menu
)    
    await state.set_state(arenda_uy.kuchmas_mulk)


@dp.message(arenda_uy.kuchmas_mulk)
async def kuch_mulk(message: types.Message, state: FSMContext):
    await state.update_data(kuchmas_mulk=message.text)
    await message.answer(f"""
Qancha muddatga ijara ga berasiz?

Tugmalardan birini tanlang 👇
""", reply_markup=muddat_menu
)    
    await state.set_state(arenda_uy.muddat)


@dp.message(arenda_uy.muddat)
async def muddat(message: types.Message, state: FSMContext):
    await state.update_data(muddat=message.text)
    await message.answer(f"""
Qaysi viloyatda joylashgan?

Tugmalardan birini tanlang 👇
""", reply_markup=viloyat_menu
    )
    await state.set_state(arenda_uy.viloyat)


@dp.message(arenda_uy.viloyat)
async def viloyat(message: types.Message, state: FSMContext):
    await state.update_data(viloyat=message.text)
    await message.answer("""
Qaysi Tumanda?

Tugmalardan birini tanlang 👇
""", reply_markup=toshkent_tuman)
    await state.set_state(arenda_uy.tuman)


@dp.message(arenda_uy.tuman)
async def tuman(message: types.Message, state: FSMContext):
    await state.update_data(tuman=message.text)
    await message.answer("""
Necha xona?

Tugmalardan birini tanlang 👇
""", reply_markup=xona_menu)
    await state.set_state(arenda_uy.xona)


@dp.message(arenda_uy.xona)
async def xona1(message: types.Message, state: FSMContext):
    await state.update_data(xona=message.text)
    await message.answer("""
Maydoni necha kvadrat bo'lsin? (m²)

Tugmalardan birini tanlang. 👇
""", reply_markup=maydon_menu)
    await state.set_state(arenda_uy.maydon)


@dp.message(arenda_uy.maydon)
async def maydon(message: types.Message, state: FSMContext):
    await state.update_data(maydon=message.text)
    await message.answer("""
Ta'miri qanday?

Tugmalardan birini tanlang 👇
""", reply_markup=tamir_menu)
    await state.set_state(arenda_uy.tamir)


@dp.message(arenda_uy.tamir)
async def tamir(message: types.Message, state: FSMContext):
    await state.update_data(tamir=message.text)
    await message.answer("""
Binoda bor qo'shimcha jihozlarni quyidagi tugmalar yordamida tanlang 👇
""", reply_markup=jihoz_menu)
    await state.set_state(arenda_uy.jihoz_uy)

@dp.message(arenda_uy.jihoz_uy)
async def jihoz_uy(message: types.Message, state: FSMContext):
    await state.update_data(jihoz_uy=message.text)
    await message.answer("""
📎 Shu belgini bosib rasmlarni yuklang.

Yuklangan 1-rasm asosiy qilib belgilanadi.

❗️Rasm tanlaganigizdan keyin tizim rasmlarni yuklab olish uchun 5-6 soniya kutib turing.️
""", reply_markup=barchasini_tanlang)
    await state.set_state(arenda_uy.rasim)


@dp.message(arenda_uy.rasim)
async def rasim(message: types.Message, state: FSMContext):
    await state.update_data(rasim=message.photo[-1].file_id)
    await message.answer("""
Narxi qancha? (1 oy uchun)

Tugmalardan birini tanlang 👇
""", reply_markup=narx)
    await state.set_state(arenda_uy.narx)

@dp.message(arenda_uy.narx)
async def narx2(message: types.Message, state: FSMContext):
    await state.update_data(narx=message.text)
    await message.answer("""
Makler haqi bormi?

Agar bo'lsa nechi foiz?

Makler haqi yo'q bo'lsa YO'Q tugmasini bosing 👇
""", reply_markup=makler_narx)
    await state.set_state(arenda_uy.makler)


@dp.message(arenda_uy.makler)
async def makler(message: types.Message, state: FSMContext):
    await state.update_data(makler=message.text)
    await message.answer("""
Telefon raqamni yuborish tugmasini bosing,

yoki boshqa raqamingizni shu ko'rinishda yozing!
 
👉 +998901234567
""", reply_markup=telefon_raqam)
    await state.set_state(arenda_uy.tel_raqam)


@dp.message(arenda_uy.tel_raqam)
async def tel_raqam(message: types.Message, state: FSMContext):
    await state.update_data(tel_raqam=message.text)
    data = await state.get_data()

    text = f"""
🌟IJARA-CHI | KVARTIRA, {data.get('kuchmas_mulk')}

🏦 KUCHMAS MULK:  {data.get('kuchmas_mulk')}
⏰ MUDDAT:  {data.get('muddat')}
🏔️ VILOYAT:  {data.get('viloyat')}
🏙 TUMAN:  {data.get('tuman')}
🚪 NECHA XONA:  {data.get('xona')}
🏡 MAYDON:  {data.get('maydon')}
🛠️ TAMIR:  {data.get('tamir')}
🛏️ JIHOZLAR:  {data.get('jihoz_state')}
💵 NARX:  {data.get('narx')}
💳 MAKLER:   {data.get('makler')}

✏️ @{message.from_user.username}
"""

    # await state.clear()
    await message.answer_photo(photo=data.get('rasim'), caption=text)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
