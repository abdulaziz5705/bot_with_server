from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

keyboard = InlineKeyboardMarkup()
button1 = InlineKeyboardButton(text="➖", callback_data="option1")
button2 = InlineKeyboardButton(text="1", callback_data="option2")
button3 = InlineKeyboardButton(text="➕", callback_data="option3")
button4 = InlineKeyboardButton(text="Back", callback_data="option3")
keyboard.add(button1, button2, button3, button4)
# keyboard.add(button4)
