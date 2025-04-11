from aiogram import F, Router
from aiogram.filters import CommandStart

import app.keyboard as kb

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


@router.callback_query(F.data == 'to_categories')
async def to_categories(callback):
    await callback.message.edit_text('Categories', reply_markup=kb.categories_buttons)


@router.callback_query(F.data == 'outerwear')
async def show_outerwear(callback):
    await callback.message.edit_text('Select your outerwear:', reply_markup=await kb.show_outerwear())


@router.callback_query(F.data == 'underwear')
async def show_underwear(callback):
    await callback.message.edit_text('Select your underwear:', reply_markup=await kb.show_underwear())


@router.callback_query(F.data == 'footwear')
async def show_footwear(callback):
    await callback.message.edit_text('Select your footwear:', reply_markup=await kb.show_footwear())


@router.callback_query(F.data.startswith('outerwear_'))
async def show_good_outerwear(callback):
    good = callback.data.split('_')[1]
    await callback.message.edit_text(good)


@router.callback_query(F.data.startswith('underwear_'))
async def show_good_underwear(callback):
    good = callback.data.split('_')[1]
    await callback.message.edit_text(good)


@router.callback_query(F.data.startswith('footwear_'))
async def show_good_footwear(callback):
    good = callback.data.split('_')[1]
    await callback.message.edit_text(good)


@router.callback_query(F.data == 'all_goods')
async def show_all_goods_handler(callback):
    await callback.message.edit_text('All goods:', reply_markup=await kb.show_all_goods())


@router.callback_query(F.data.startswith('all_'))
async def show_good_from_all(callback):
    good = callback.data.split('_', maxsplit=1)[1]
    await callback.message.edit_text(f"{good}")
