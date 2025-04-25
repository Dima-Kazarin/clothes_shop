from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from products import products

ITEMS_PER_PAGE = 5

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

good_buttons = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='◀️', callback_data='from_good_to_main'),
     InlineKeyboardButton(text='🛍️', callback_data='add_to_cart')],
])


async def show_outerwear(page):
    outerwears = []
    for product in products:
        if product['name'].lower().startswith('худі'):
            outerwears.append(product)
        elif product['name'].lower().startswith('світшот'):
            outerwears.append(product)
        elif product['name'].lower().startswith('футболка'):
            outerwears.append(product)
        elif product['name'].lower().startswith('куртка'):
            outerwears.append(product)
        elif product['name'].lower().startswith('пуховик'):
            outerwears.append(product)
        elif product['name'].lower().startswith('вітровка'):
            outerwears.append(product)
        elif product['name'].lower().startswith('бомбер'):
            outerwears.append(product)

    keyboard = InlineKeyboardBuilder()

    start = page * ITEMS_PER_PAGE
    end = start + ITEMS_PER_PAGE
    goods_slice = outerwears[start:end]

    for good in goods_slice:
        keyboard.add(InlineKeyboardButton(text=good['name'], callback_data=f'good_{good["name"].split(" ")[-1]}'))

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
    underwears = []
    for product in products:
        if product['name'].lower().startswith('джинси'):
            underwears.append(product)
        elif product['name'].lower().startswith('шорти'):
            underwears.append(product)

    keyboard = InlineKeyboardBuilder()

    start = page * ITEMS_PER_PAGE
    end = start + ITEMS_PER_PAGE
    goods_slice = underwears[start:end]

    for good in goods_slice:
        keyboard.add(InlineKeyboardButton(text=good['name'], callback_data=f'good_{good["name"].split(" ")[-1]}'))

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
    footwears = []
    for product in products:
        if product['name'].lower().startswith('кеди'):
            footwears.append(product)
        elif product['name'].lower().startswith('кросівки'):
            footwears.append(product)
        elif product['name'].lower().startswith('тапочки'):
            footwears.append(product)

    keyboard = InlineKeyboardBuilder()

    start = page * ITEMS_PER_PAGE
    end = start + ITEMS_PER_PAGE
    goods_slice = footwears[start:end]

    for good in goods_slice:
        keyboard.add(InlineKeyboardButton(text=good['name'], callback_data=f'good_{good["name"].split(" ")[-1]}'))

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
        keyboard.add(InlineKeyboardButton(text=good['name'], callback_data=f'good_{good["name"].split(" ")[-1]}'))

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
