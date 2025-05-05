from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
import json

with open('products.json', 'r', encoding='utf-8') as file:
    products = json.load(file)

with open('outwear_products.json', 'r', encoding='utf-8') as file:
    outerwears = json.load(file)

with open('underwear_products.json', 'r', encoding='utf-8') as file:
    underwears = json.load(file)

with open('footwear_products.json', 'r', encoding='utf-8') as file:
    footwears = json.load(file)


ITEMS_PER_PAGE = 5

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Catalog')],
    [KeyboardButton(text='Open Cart')]
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

good_buttons = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='◀️', callback_data='from_good_to_main'),
     InlineKeyboardButton(text='🛍️', callback_data='add_to_cart')],
])


async def show_outerwear(page):
    keyboard = InlineKeyboardBuilder()

    start = page * ITEMS_PER_PAGE
    end = start + ITEMS_PER_PAGE
    goods_slice = outerwears[start:end]

    for good in goods_slice:
        keyboard.add(InlineKeyboardButton(text=good['name'], callback_data=f'good_{good["id"]}'))

    keyboard.adjust(1)

    nav_buttons = []
    if page > 0:
        nav_buttons.append(InlineKeyboardButton(text='◀️', callback_data=f'outerwearpage_{page - 1}'))
    nav_buttons.append(InlineKeyboardButton(text='🏠', callback_data='to_categories'))
    if end < len(outerwears):
        nav_buttons.append(InlineKeyboardButton(text='▶️', callback_data=f'outerwearpage_{page + 1}'))

    if nav_buttons:
        keyboard.row(*nav_buttons)

    return keyboard.as_markup()


async def show_underwear(page):
    keyboard = InlineKeyboardBuilder()

    start = page * ITEMS_PER_PAGE
    end = start + ITEMS_PER_PAGE
    goods_slice = underwears[start:end]

    for good in goods_slice:
        keyboard.add(InlineKeyboardButton(text=good['name'], callback_data=f'good_{good["id"]}'))

    keyboard.adjust(1)

    nav_buttons = []
    if page > 0:
        nav_buttons.append(InlineKeyboardButton(text='◀️', callback_data=f'underwearpage_{page - 1}'))
    nav_buttons.append(InlineKeyboardButton(text='🏠', callback_data='to_categories'))
    if end < len(underwears):
        nav_buttons.append(InlineKeyboardButton(text='▶️', callback_data=f'underwearpage_{page + 1}'))

    if nav_buttons:
        keyboard.row(*nav_buttons)

    return keyboard.as_markup()


async def show_footwear(page):
    keyboard = InlineKeyboardBuilder()

    start = page * ITEMS_PER_PAGE
    end = start + ITEMS_PER_PAGE
    goods_slice = footwears[start:end]

    for good in goods_slice:
        keyboard.add(InlineKeyboardButton(text=good['name'], callback_data=f'good_{good["id"]}'))

    keyboard.adjust(1)

    nav_buttons = []
    if page > 0:
        nav_buttons.append(InlineKeyboardButton(text='◀️', callback_data=f'footwearpage_{page - 1}'))
    nav_buttons.append(InlineKeyboardButton(text='🏠', callback_data='to_categories'))
    if end < len(footwears):
        nav_buttons.append(InlineKeyboardButton(text='▶️', callback_data=f'footwearpage_{page + 1}'))

    if nav_buttons:
        keyboard.row(*nav_buttons)

    return keyboard.as_markup()


async def show_all_goods(page):
    all_goods = products
    keyboard = InlineKeyboardBuilder()

    start = page * ITEMS_PER_PAGE
    end = start + ITEMS_PER_PAGE
    goods_slice = all_goods[start:end]

    for good in goods_slice:
        keyboard.add(InlineKeyboardButton(text=good['name'], callback_data=f'good_{good["id"]}'))

    keyboard.adjust(1)

    nav_buttons = []
    if page > 0:
        nav_buttons.append(InlineKeyboardButton(text='◀️', callback_data=f'page_{page - 1}'))
    nav_buttons.append(InlineKeyboardButton(text='🏠', callback_data='to_main'))
    if end < len(all_goods):
        nav_buttons.append(InlineKeyboardButton(text='▶️', callback_data=f'page_{page + 1}'))

    if nav_buttons:
        keyboard.row(*nav_buttons)

    return keyboard.as_markup()


async def add_good_buttons(good_id):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='🛒 Add to cart', callback_data=f'add_to_cart_{good_id}')],
            [InlineKeyboardButton(text='🔙 Back', callback_data='from_good_to_main')]
        ]
    )

cart_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='🏠', callback_data='to_main')],
    ]
)