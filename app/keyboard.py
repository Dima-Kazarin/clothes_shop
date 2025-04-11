from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

outerwears = ['T1', 'T2', 'T3']
underwears = ['T4', 'T5', 'T6']
footwears = ['T7', 'T8', 'T9']

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Catalog')]
], resize_keyboard=True)

filter_buttons = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='All', callback_data='all_goods')],
    [InlineKeyboardButton(text='Categories', callback_data='categories')]
])

categories_buttons = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Outerwear', callback_data='outerwear')],
    [InlineKeyboardButton(text='Underwear', callback_data='underwear')],
    [InlineKeyboardButton(text='Footwear', callback_data='footwear')],
    [InlineKeyboardButton(text='◀️', callback_data='to_main')],
])


async def show_outerwear():
    keyboard = InlineKeyboardBuilder()
    for good in outerwears:
        keyboard.add(InlineKeyboardButton(text=good, callback_data=f'outerwear_{good}'))
    keyboard.add(InlineKeyboardButton(text='◀️', callback_data='to_categories'))

    return keyboard.adjust(1).as_markup()


async def show_underwear():
    keyboard = InlineKeyboardBuilder()
    for good in underwears:
        keyboard.add(InlineKeyboardButton(text=good, callback_data=f'underwear_{good}'))
    keyboard.add(InlineKeyboardButton(text='◀️', callback_data='to_categories'))

    return keyboard.adjust(1).as_markup()


async def show_footwear():
    keyboard = InlineKeyboardBuilder()
    for good in footwears:
        keyboard.add(InlineKeyboardButton(text=good, callback_data=f'footwear_{good}'))
    keyboard.add(InlineKeyboardButton(text='◀️', callback_data='to_categories'))

    return keyboard.adjust(1).as_markup()
