import requests
from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import InputMediaPhoto, InputFile, URLInputFile

import app.keyboard as kb
from products import products

router = Router()


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
    await callback.message.delete()

    good_id = callback.data.split('_')[1]
    for product in products:
        if product['name'].endswith(good_id):
            good = product

    message_text = f'{" ".join(good["name"].split(" ")[:-1])}\n'
    message_text += f'Розміри: {", ".join(good["sizes"])}\n'
    message_text += f'Ціна: {good["price"]}\n'

    photo = URLInputFile(good['photo'])
    await callback.message.answer_photo(photo, caption=message_text, reply_markup=kb.good_buttons)


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
