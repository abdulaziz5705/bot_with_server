import os
import logging
from aiogram import Bot, Dispatcher, executor, types
from default_button import (menu_keyboard, menu_detail, mahsulot_button, menu_kiyim, menu_avto, menu_detail4,
                            menu_detail5, menu_detail6, menu_detail7, menu_detail8, rang)
import asyncio
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    full_name = message.from_user.full_name
    username = message.from_user.username
    await message.reply(f"Welcome {full_name}", reply_markup=menu_keyboard)


@dp.message_handler(lambda message: message.text == "Kitoblar")
async def show_menu(message: types.Message):
    #action = button_callback_menu.new(action=message.text)
    await message.answer("1 - bo'lim. Mahsulotlardan birini tanglang:", reply_markup=menu_detail)


@dp.message_handler(lambda message: message.text == "Kiyimlar")
async def show_menu(message: types.Message):
    await message.answer("2 - bo'lim. Mahsulotlardan birini tanglang: ", reply_markup=menu_kiyim)


@dp.message_handler(lambda message: message.text == "Avtotovarlar")
async def show_menu(message: types.Message):
    await message.answer("3 - bo'lim. Mahsulotlardan birini tanglang: ", reply_markup=menu_avto)


@dp.message_handler(lambda message: message.text == "Texnika")
async def show_menu(message: types.Message):
    await message.answer("4 - bo'lim. Mahsulotlardan birini tanglang: ", reply_markup=menu_detail4)


@dp.message_handler(lambda message: message.text == "Oyoq Kiyimlar")
async def show_menu(message: types.Message):
    await message.answer("5 - bo'lim. Mahsulotlardan birini tanglang: ", reply_markup=menu_detail5)


@dp.message_handler(lambda message: message.text == "Akksessuar")
async def show_menu(message: types.Message):
    await message.answer("6 - bo'lim. Mahsulotlardan birini tanglang: ", reply_markup=menu_detail6)


@dp.message_handler(lambda message: message.text == "Remont")
async def show_menu(message: types.Message):
    await message.answer("7 - bo'lim. Mahsulotlardan birini tanglang: ", reply_markup=menu_detail7)


@dp.message_handler(lambda message: message.text == "Kanstovar")
async def show_menu(message: types.Message):
    await message.answer("8 - bo'lim. Mahsulotlardan birini tanglang: ", reply_markup=menu_detail8)


@dp.message_handler(lambda message: message.text == "Atom Habits")
async def show_menu(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="➖", callback_data="option1")
    button2 = types.InlineKeyboardButton(text="1", callback_data="option2")
    button3 = types.InlineKeyboardButton(text="➕", callback_data="option3")
    #button4 = types.InlineKeyboardButton(text="Back", reply_markup=menu_detail
    keyboard.add(button1, button2, button3)
    await bot.send_message(message.chat.id, "Mahsulot sonini tanlang: ", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "Back")
async def show_menu(message: types.Message):
    await message.answer("Menyulardan birini tanglang:", reply_markup=menu_keyboard)


@dp.message_handler(lambda message: message.text == "Mahsulot 1")
async def show_menu(message: types.Message):
    await message.answer("2 - bo'lim. Mahsulotlardan birini tanglang:", reply_markup=mahsulot_button)


@dp.message_handler(lambda message: message.text == "Futbolka")
async def show_menu(message: types.Message):
    await message.answer("Mahsulot rangini tanlang:", reply_markup=rang)


@dp.message_handler(lambda message: message.text == "Bryuki")
async def show_menu(message: types.Message):
    await message.answer("Mahsulot rangini tanlang:", reply_markup=rang)


@dp.message_handler(lambda message: message.text == "Triko")
async def show_menu(message: types.Message):
    await message.answer("Mahsulot rangini tanlang:", reply_markup=rang)


@dp.message_handler(lambda message: message.text == "Kuylak")
async def show_menu(message: types.Message):
    await message.answer("Mahsulot rangini tanlang:", reply_markup=rang)


@dp.message_handler(lambda message: message.text == "Qora")
async def show_menu(message: types.Message):
    await message.answer("Color is successfully select:", reply_markup=menu_kiyim)


@dp.message_handler(lambda message: message.text == "Oq")
async def show_menu(message: types.Message):
    await message.answer("Color is successfully select:", reply_markup=menu_kiyim)


@dp.message_handler(lambda message: message.text == "Kuk")
async def show_menu(message: types.Message):
    await message.answer("Color is successfully select:", reply_markup=menu_kiyim)


@dp.message_handler(lambda message: message.text == "Yashil")
async def show_menu(message: types.Message):
    await message.answer("Color is successfully select:", reply_markup=menu_kiyim)


@dp.message_handler(lambda message: message.text == "Qora")
async def show_menu(message: types.Message):
    await message.answer("Color is successfully select:", reply_markup=menu_kiyim)


@dp.message_handler(commands=['image'])
async def send_image(message: types.Message):
    #Pastgi kodda admin qismini qo'shishingiz mumkun listni ichiga telegram id kiritasiz
    if message.from_user.id in []:
        await message.reply("Salom admin")
        photo_path = "telegram_bot/img.png"
        await bot.send_photo(message.chat.id, photo=photo_path)
    else:
        await message.reply("Bunday buyruq turi mavjud emas")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
