from parser_config import *
from parser_utils import *
import os
import math
import time
from tqdm import tqdm
from colorama import Fore, init


init(autoreset=True)

def get_data(categories_ids, region, saved_file_name):

    products = {}

    s = requests.Session()

    if not os.path.exists('data'):
        os.mkdir('data')

    cookies.update({'MVID_REGION_SHOP': region})

    for category in categories_ids:
        params = {
            'categoryIds': category,
            'offset': '0',
            'filterParams': 'WyJ0b2xrby12LW5hbGljaGlpIiwiLTEyIiwiZGEiXQ==',
            'limit': '49',
            'doTranslit': 'true',
            'context': 'v2dzaG9wX2lkZFM5NTVsY2F0ZWdvcnlfaWRzn2MyMDX/ZmNhdF9JZGMyMDX/',
        }
        response = try_request(s, 'get', 'https://www.mvideo.ru/bff/products/v2/search',
                               params=params, cookies=cookies, headers=headers)
        shutdown_scenario(response, saved_file_name, products)
        total_items = response.get('body').get('total')

        total_pages = math.ceil(total_items / 48)
        #tqdm.write(f'{Fore.LIGHTBLUE_EX}{total_items} ITEMS READY TO PARSE IN CATEGORY {category}')
        progress_bar = tqdm(total=total_items, desc=f'PARSING CATEGORY {category}',
                            bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt}', ncols=100)

        for i in range(total_pages):

            offset = f'{i * 48}'
            params = {
                'categoryIds': category,
                'offset': offset,
                'filterParams': 'WyJ0b2xrby12LW5hbGljaGlpIiwiLTEyIiwiZGEiXQ==',
                'limit': '48',
                'doTranslit': 'true',
                'context': 'v2dzaG9wX2lkZFM5NTVsY2F0ZWdvcnlfaWRzn2MyMDX/ZmNhdF9JZGMyMDX/',
            }
            response = try_request(s, 'get', 'https://www.mvideo.ru/bff/products/v2/search',
                                   params=params, cookies=cookies, headers=headers)
            shutdown_scenario(response, saved_file_name, products)
            products_ids_list = response.get('body').get('products')

            json_data = {
                'productIds': products_ids_list,
                'mediaTypes': [
                    'images',
                ],
                'category': True,
                'status': True,
                'brand': True,
                'propertyTypes': [
                    'KEY',
                ],
                'propertiesConfig': {
                    'propertiesPortionSize': 5,
                },
            }
            response = try_request(s, 'post', 'https://www.mvideo.ru/bff/product-details/list',
                                   cookies=cookies, headers=headers, json=json_data)
            shutdown_scenario(response, saved_file_name, products)

            parsed_products = {
                i.get('productId'): {
                    'name': i.get('name'),
                    'id': i.get('productId'),
                    'link': 'https://www.mvideo.ru/products/' + i.get('productId')
                } for i in response.get('body').get('products')
            }

            products.update(parsed_products)
            progress_bar.update(len(parsed_products))

            product_ids_str = ','.join(products_ids_list)
            params = {
                'productIds': product_ids_str,
                'addBonusRubles': 'true',
                'isPromoApplied': 'true',
            }

            time.sleep(random.uniform(3,5))
            response = try_request(s, 'get', 'https://www.mvideo.ru/bff/products/prices',
                                   params=params, cookies=cookies, headers=headers)
            shutdown_scenario(response, saved_file_name, products)
            prices = response.get('body').get('materialPrices')

            prices_map = {
                item['price']['productId']: {
                    'price': item['price']['basePrice'],
                    'sale_price': item['price']['salePrice']
                } for item in prices
            }

            for product_id, price in prices_map.items():
                if product_id in products:
                    products[product_id].update(price)

        progress_bar.close()
        tqdm.write(f'{Fore.LIGHTGREEN_EX}PARSING CATEGORY {category}: DONE\n')

    save_data(saved_file_name, products)
    tqdm.write(f'{Fore.LIGHTGREEN_EX}PARSING CATEGORIES IN REGION {region}: DONE\n'
               f'DATA SAVED IN data/{saved_file_name}.json\n')

def prices_compare(file_old, file_new):
    products_old = read_data(file_old)

    products_new = read_data(file_new)

    diff_products = {}

    for product_id, product_data in products_old.items():
        if product_id in products_new:
            if product_data['sale_price'] < products_new[product_id]['sale_price']:
                diff_products.update({
                    product_id: {
                        'name': product_data['name'],
                        'link': product_data['link'],
                        'old_price': product_data['sale_price'],
                        'new_price': products_new[product_id]['sale_price']
                    }
                })

    save_data('prices_diff', diff_products)
    tqdm.write(f'{Fore.LIGHTGREEN_EX}DIFFERENCES FOUND: {len(diff_products)}\nDATA SAVED IN data/prices_diff.json')



def main():
    get_data(categories, 'S002', 'products_moscow')
    get_data(categories, 'S955', 'products_novosibirsk')
    prices_compare('products_moscow', 'products_novosibirsk')


if __name__ == '__main__':
    main()
