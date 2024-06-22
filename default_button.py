from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from inline_button import keyboard


menu_keyboard = ReplyKeyboardMarkup([
    [KeyboardButton("Kitoblar"), KeyboardButton("Kiyimlar "), KeyboardButton("Avtotovarlar ")],
    [KeyboardButton("Texnika "), KeyboardButton("Oyoq Kiyimlar "), KeyboardButton("Akksessuar ")],
    [KeyboardButton("Remont ")],
    [KeyboardButton("Kanstovar ")],
],
    resize_keyboard=True)

# async def get_all_product():
# Kitoblarni ro'yhati
menu_detail = ReplyKeyboardMarkup(resize_keyboard=True)

menu_detail.add(KeyboardButton("Atom Habits"), KeyboardButton("Ullamolar nazlida vaqtnning qadri "))
menu_detail.add(KeyboardButton("Izlash "), KeyboardButton("Nikolas Sparks "))
menu_detail.add(KeyboardButton("Back"))

mahsulot_button = ReplyKeyboardMarkup(resize_keyboard=True)
mahsulot_button.add(KeyboardButton("Back"))

#Kiyimlar ro'yhati
menu_kiyim = ReplyKeyboardMarkup(resize_keyboard=True)

menu_kiyim.add(KeyboardButton("Futbolka"), KeyboardButton("Bryuki "))
menu_kiyim.add(KeyboardButton("Triko "), KeyboardButton("Kuylak"))
menu_kiyim.add(KeyboardButton("Back"))

mahsulot_button = ReplyKeyboardMarkup(resize_keyboard=True)
mahsulot_button.add(KeyboardButton("Back"))

#Avtotovarlar ro'yhati
menu_avto = ReplyKeyboardMarkup(resize_keyboard=True)

menu_avto.add(KeyboardButton("Shina"), KeyboardButton("Bar "))
menu_avto.add(KeyboardButton("Chexol "), KeyboardButton("Diska "))
menu_avto.add(KeyboardButton("Back"))

mahsulot_button = ReplyKeyboardMarkup(resize_keyboard=True)
mahsulot_button.add(KeyboardButton("Back"))

#Texnika ro'yhati
menu_detail4 = ReplyKeyboardMarkup(resize_keyboard=True)
menu_detail4.add(KeyboardButton("Xolodelnik "), KeyboardButton("Dazmol "))
menu_detail4.add(KeyboardButton("Gazplita"), KeyboardButton("Pech "))
menu_detail4.add(KeyboardButton("Back"))

mahsulot_button = ReplyKeyboardMarkup(resize_keyboard=True)
mahsulot_button.add(KeyboardButton("Back"))

#Oyoq kiyimlar ro'yhati
menu_detail5 = ReplyKeyboardMarkup(resize_keyboard=True)
menu_detail5.add(KeyboardButton("Krassofki"), KeyboardButton("Tufli"))
menu_detail5.add(KeyboardButton("Mokasini "), KeyboardButton("Cheshki"))
menu_detail5.add(KeyboardButton("Back"))

mahsulot_button = ReplyKeyboardMarkup(resize_keyboard=True)
mahsulot_button.add(KeyboardButton("Back"))

#Akksessuarlar ro'yhat
menu_detail6 = ReplyKeyboardMarkup(resize_keyboard=True)
menu_detail6.add(KeyboardButton("Ochki "), KeyboardButton("Kolso "))
menu_detail6.add(KeyboardButton("Sumka "), KeyboardButton("RFID "))
menu_detail6.add(KeyboardButton("Back"))

mahsulot_button = ReplyKeyboardMarkup(resize_keyboard=True)
mahsulot_button.add(KeyboardButton("Back"))

#Remont tovarlar
menu_detail7 = ReplyKeyboardMarkup(resize_keyboard=True)
menu_detail7.add(KeyboardButton(" Elektr uzatgich"), KeyboardButton("Shurupburagich to'plami"))
menu_detail7.add(KeyboardButton("Magnitliy otvyortkalar"), KeyboardButton("Lenta o'lchovi"))
menu_detail7.add(KeyboardButton("Back"))

mahsulot_button = ReplyKeyboardMarkup(resize_keyboard=True)
mahsulot_button.add(KeyboardButton("Back"))

#Kanstovar ro'yhati
menu_detail8 = ReplyKeyboardMarkup(resize_keyboard=True)
menu_detail8.add(KeyboardButton("Qog'oz A4"), KeyboardButton("Ruchka"))
menu_detail8.add(KeyboardButton("Izlash "), KeyboardButton("Marker "))
menu_detail8.add(KeyboardButton("Back"))

mahsulot_button = ReplyKeyboardMarkup(resize_keyboard=True)
mahsulot_button.add(KeyboardButton("Back"))

#rang
rang = ReplyKeyboardMarkup(resize_keyboard=True)
rang.add(KeyboardButton("Qora"), KeyboardButton("Oq"))
rang.add(KeyboardButton("Kuk "), KeyboardButton("Yashil "))
rang.add(KeyboardButton("Back"))

mahsulot_button = ReplyKeyboardMarkup(resize_keyboard=True)
mahsulot_button.add(KeyboardButton("Back"))
