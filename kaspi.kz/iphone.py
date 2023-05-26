import json
import time

from bs4 import BeautifulSoup
import lxml
import requests


def parsing():
    pages = int(input('Количество страниц для парсинга: '))
    result_items = []
    for page in range(0, pages):
        time.sleep(2)
        url = f'https://kaspi.kz/yml/product-view/pl/results?page={page}&q=%3Acategory%3ASmartphones%3AmanufacturerName%3AApple%3AavailableInZones%3AMagnum_ZONE1&text&sort=relevance&qs&ui=d&i=-1'
        cookies = {
            'ks.ngs.s': '02c49e1e4cf891b56970f56f32e28721',
            'k_stat': '2bdb59b6-0a72-450e-9a2e-a0e9924c63d7',
            'ks.tg': '99',
            '_hjFirstSeen': '1',
            '_hjIncludedInSessionSample': '1',
            '_hjSession_283363': 'eyJpZCI6IjJjOGM4MjVmLTU1NDUtNDhiOC1hMTdmLWRjZDU3ZDQwODY1NiIsImNyZWF0ZWQiOjE2ODUwOTA1MDU0MjksImluU2FtcGxlIjp0cnVlfQ==',
            '_hjAbsoluteSessionInProgress': '0',
            'ssaid': '260e6f20-fba1-11ed-af57-438a1d20ec80',
            '_ga': 'GA1.2.174913791.1685090507',
            '_gid': 'GA1.2.1954664680.1685090507',
            '_ym_uid': '16850905086625167',
            '_ym_d': '1685090508',
            '_ym_isad': '1',
            '_ym_visorc': 'b',
            'kaspi.storefront.cookie.city': '750000000',
            '_hjSessionUser_283363': 'eyJpZCI6IjEzYTlkOWIzLWIzYjktNWNmOC1iYWQzLWJlMjJkNGZmZDVjNSIsImNyZWF0ZWQiOjE2ODUwOTA1MDUyMjksImV4aXN0aW5nIjp0cnVlfQ==',
            '__tld__': 'null',
            '_gali': 'scroll-to',
        }

        headers = {
            'Accept': 'application/json, text/*',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            # 'Cookie': 'ks.ngs.s=02c49e1e4cf891b56970f56f32e28721; k_stat=2bdb59b6-0a72-450e-9a2e-a0e9924c63d7; ks.tg=99; _hjFirstSeen=1; _hjIncludedInSessionSample=1; _hjSession_283363=eyJpZCI6IjJjOGM4MjVmLTU1NDUtNDhiOC1hMTdmLWRjZDU3ZDQwODY1NiIsImNyZWF0ZWQiOjE2ODUwOTA1MDU0MjksImluU2FtcGxlIjp0cnVlfQ==; _hjAbsoluteSessionInProgress=0; ssaid=260e6f20-fba1-11ed-af57-438a1d20ec80; _ga=GA1.2.174913791.1685090507; _gid=GA1.2.1954664680.1685090507; _ym_uid=16850905086625167; _ym_d=1685090508; _ym_isad=1; _ym_visorc=b; kaspi.storefront.cookie.city=750000000; _hjSessionUser_283363=eyJpZCI6IjEzYTlkOWIzLWIzYjktNWNmOC1iYWQzLWJlMjJkNGZmZDVjNSIsImNyZWF0ZWQiOjE2ODUwOTA1MDUyMjksImV4aXN0aW5nIjp0cnVlfQ==; __tld__=null; _gali=scroll-to',
            'Pragma': 'no-cache',
            'Referer': 'https://kaspi.kz/shop/c/smartphones/?q=%3AavailableInZones%3AMagnum_ZONE1%3Acategory%3ASmartphones%3AmanufacturerName%3AApple&sort=relevance&sc=',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        response = requests.get(
            url,
            cookies=cookies,
            headers=headers,
        ).json()

        print(f'Страница {page} пройдена успешно!')
        time.sleep(2)
        print('Сортируем и добавляем в список')
        time.sleep(3)

        def sorting_data(sorting: dict):
            found_data = sorting.get('data')
            count = 0
            for items in found_data:

                result_items.append({
                    'id': items.get('id'),
                    'title': items.get('title'),
                    'brand': items.get('brand'),
                    'price': items.get('unitPrice'),
                    'shopLink': items.get('shopLink')
                })

                count += 1
            print(f'На {page} стринице\nКоличество товара: {count}')
        sorting_data(response)
        time.sleep(3)
        print('Переходим к следующей странице\n')
    return result_items


def file_creation(parsing_data: list):
    file_name = str(input('Как назвать файл?: '))
    with open(f'{file_name}.json', 'a', encoding='utf8') as file:
        json.dump(parsing_data, file, indent=4, sort_keys=True)



if __name__ == '__main__':
    file_creation(parsing())