from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

cars_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Inomarka"), 
        ],

        [
           KeyboardButton(text="Chevrolet")
        ]
    ],
    resize_keyboard=True
)


chevrolet_cars = ReplyKeyboardMarkup(

    keyboard=[
        [
            KeyboardButton(text="Cobalt"),
            KeyboardButton(text="Malibu")
        ],

        [
            KeyboardButton(text="Tracker"),
            KeyboardButton(text="Nexia_2") 
        ],
        [
            KeyboardButton(text="⏪Orqaga")
        ]
    ],
    resize_keyboard=True,
)

inomarka_cars = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Li_9"),
            KeyboardButton(text="Kia_k5")
        ],
        [
            KeyboardButton(text="Tesla"),
            KeyboardButton(text="Toyota_Camry")
        ],
        [
            KeyboardButton(text="⏪Orqaga")
        ]
    ],
    resize_keyboard=True,
)

