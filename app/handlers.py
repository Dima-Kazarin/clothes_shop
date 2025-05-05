import json
import os
from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.exceptions import TelegramNetworkError

import app.keyboard as kb

router = Router()
CART_FILE = 'cart.json'

file_path = 'products.json'

with open(file_path, 'r', encoding='utf-8') as file:
    products = json.load(file)

@router.message(CommandStart())
async def start(message):
    await message.answer('Hello', reply_markup=kb.main)


@router.message(F.text == 'Catalog')
async def handle_catalog(message):
    await message.answer('What products would you like to see?', reply_markup=kb.filter_buttons)


@router.callback_query(F.data == 'categories')
async def show_categories(callback):
    await callback.message.edit_text('Categories', reply_markup=kb.categories_buttons)


@router.callback_query(F.data == 'to_main')
async def to_main(callback):
    await callback.message.edit_text('What products would you like to see?', reply_markup=kb.filter_buttons)


@router.callback_query(F.data == 'from_good_to_main')
async def from_good_to_main(callback):
    await callback.message.delete()
    await callback.message.answer('What products would you like to see?', reply_markup=kb.filter_buttons)


@router.callback_query(F.data == 'to_categories')
async def to_categories(callback):
    await callback.message.edit_text('Categories', reply_markup=kb.categories_buttons)


@router.callback_query(F.data == 'outerwear')
async def show_outerwear(callback):
    await callback.message.edit_text('Select your outerwear:', reply_markup=await kb.show_outerwear(page=0))


@router.callback_query(F.data == 'underwear')
async def show_underwear(callback):
    await callback.message.edit_text('Select your underwear:', reply_markup=await kb.show_underwear(page=0))


@router.callback_query(F.data == 'footwear')
async def show_footwear(callback):
    await callback.message.edit_text('Select your footwear:', reply_markup=await kb.show_footwear(page=0))


@router.callback_query(F.data.startswith('good_'))
async def show_good_outerwear(callback):
    try:
        good_id = callback.data.split('_')[1]
        good = next((product for product in products if product.get('id') == good_id), None)

        if not good:
            await callback.message.answer('❗ Product not found.')
            return

        message_text = f'{good["name"]}\n'
        message_text += f'Sizes: {", ".join(good["sizes"])}\n'
        message_text += f'Price: {good["price"]}\n'

        photo = good["photo"]
        await callback.message.answer_photo(photo, caption=message_text, reply_markup=await kb.add_good_buttons(good_id))
    except TelegramNetworkError:
        await callback.message.answer("❗ Network issue. Please try again later.")


@router.callback_query(F.data == 'all_goods')
async def show_all_goods_handler(callback):
    await callback.message.edit_text('All goods:', reply_markup=await kb.show_all_goods(page=0))


@router.callback_query(F.data.startswith('page_'))
async def paginate_goods(callback):
    page = int(callback.data.split('_')[1])
    await callback.message.edit_text('All goods:', reply_markup=await kb.show_all_goods(page=page))


@router.callback_query(F.data.startswith('outerwearpage_'))
async def paginate_outwear(callback):
    page = int(callback.data.split('_')[1])
    await callback.message.edit_text('Select your outerwear:', reply_markup=await kb.show_outerwear(page=page))


@router.callback_query(F.data.startswith('underwearpage_'))
async def paginate_underwear(callback):
    page = int(callback.data.split('_')[1])
    await callback.message.edit_text('Select your underwear:', reply_markup=await kb.show_underwear(page=page))


@router.callback_query(F.data.startswith('footwearpage_'))
async def paginate_footwear(callback):
    page = int(callback.data.split('_')[1])
    await callback.message.edit_text('Select your footwear:', reply_markup=await kb.show_footwear(page=page))


def add_to_cart(user_id, product):
    cart_file = 'cart.json'

    if os.path.exists(cart_file):
        with open(cart_file, 'r', encoding='utf-8') as file:
            cart = json.load(file)
    else:
        cart = []

    user_cart = [item for item in cart if item['user_id'] == user_id]

    for item in user_cart:
        if item['id'] == product['id']:
            item['quantity'] = item.get('quantity', 1) + 1
            break
    else:
        product_copy = product.copy()
        product_copy['quantity'] = 1
        product_copy['user_id'] = user_id  # Add user_id to the product
        cart.append(product_copy)

    with open(cart_file, 'w', encoding='utf-8') as file:
        json.dump(cart, file, ensure_ascii=False, indent=4)


@router.callback_query(F.data.startswith('add_to_cart_'))
async def add_to_cart_handler(callback):
    user_id = callback.from_user.id  # Get the unique user ID
    good_id = callback.data.split('_')[3]
    product = next((p for p in products if p.get('id') == good_id), None)

    if product:
        add_to_cart(user_id, product)
        await callback.answer('✅ Product added to cart!')
    else:
        await callback.answer('❌ Product not found.', show_alert=True)


@router.message(F.text == 'Open Cart')
async def open_cart_handler(message):
    user_id = message.from_user.id  # Get the unique user ID
    cart_file = 'cart.json'

    if os.path.exists(cart_file):
        with open(cart_file, 'r', encoding='utf-8') as file:
            cart = json.load(file)
    else:
        cart = []

    user_cart = [item for item in cart if item['user_id'] == user_id]

    if not user_cart:
        await message.edit_text("🛒 Your cart is empty.")
        return

    for product in user_cart:
        caption = f'{product["name"]}\nPrice: {product["price"]}\nQuantity: {product["quantity"]}'
        await message.answer(caption)

    await message.answer("What next?", reply_markup=kb.cart_buttons)