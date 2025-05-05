import os
import json
from bs4 import BeautifulSoup
import requests
import uuid

def parse_products(url, qty=5):
    page = requests.get(url)
    page.encoding = 'utf-8'
    soup = BeautifulSoup(page.text, 'html.parser')

    all_products = []

    product_cards = soup.find_all('div', class_='product_item')

    for card in product_cards[:qty]:
        name_tag = card.find('header', class_='p__info_name')
        price_tag = card.find('span', class_='product_item__new-cost')
        image_tag = card.find('img', class_='lazy nojs-hide aspect-inner')
        size_tags = card.find_all('div', class_='button button--white size_item--new t-14 relative')

        name = name_tag.text
        price = price_tag.text.replace('\u2009', ' ')
        image = image_tag.get('data-src')

        sizes = []
        for size_tag in size_tags:
            for span in size_tag.find_all('span'):
                span.decompose()
            size_text = size_tag.text
            sizes.append(size_text)

        all_products.append({
            'id': str(uuid.uuid4()),
            'name': name,
            'price': price,
            'photo': image,
            'sizes': sizes
        })

    return all_products


def load_or_parse_products():
    file_path = 'products.json'

    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    # Parse products if the file doesn't exist
    man_jacket_products = parse_products('https://kasta.ua/uk/market/muzhskaya-verhnyaya-odezhda/')
    woman_jacket_products = parse_products('https://kasta.ua/uk/market/zhenskaya-verhnyaya-odezhda/')

    man_shirt_products = parse_products('https://kasta.ua/uk/market/futbolki-muzhskie/')
    woman_shirt_products = parse_products('https://kasta.ua/uk/market/futbolki-zhenskie/')

    man_pants_products = parse_products('https://kasta.ua/uk/market/muzhskie-bryuki/')
    woman_pants_products = parse_products('https://kasta.ua/uk/market/zhenskie-bryuki/')

    man_shorts_products = parse_products('https://kasta.ua/uk/market/muzhskie-shorty/')
    woman_shorts_products = parse_products('https://kasta.ua/uk/market/shorty-zhenskie/')

    man_footwear_products = parse_products('https://kasta.ua/uk/market/muzhskaya-obuv/', 10)
    woman_footwear_products = parse_products('https://kasta.ua/uk/market/zhenskaya-obuv/', 10)

    outwear_products = man_jacket_products + man_shirt_products + woman_jacket_products + woman_shirt_products
    underwear_products = man_pants_products + man_shorts_products + woman_pants_products + woman_shorts_products
    footwear_products = man_footwear_products + woman_footwear_products

    products = outwear_products + underwear_products + footwear_products

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(products, file, ensure_ascii=False, indent=4)

    return products


# Load or parse products
products = load_or_parse_products()