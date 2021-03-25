"""
Тестовое задание 2ГИС на вакансию QA-инженер. 24.03.2020.
https://drive.google.com/file/d/1yvBPl4GnC6QOBVDrP8rpviVHZeF5B_Oo/view
"""

from requests import get
from unittest import TestCase, main

url = 'https://regions-test.2gis.com/1.0/regions'


class TestRegion(TestCase):
    def test_01_200(self):
        # Проверяем ответ сервера
        response = get(url)
        self.assertEqual(200, response.status_code, 'Ответ сервера не равен 200')

    def test_02_country_code_search(self):
        # Проверяем фильтрацию по коду страны
        response = get(f'{url}?country_code=kz')
        json_data = response.json()
        for obj in json_data['items']:
            self.assertEqual(obj['country']['code'], 'kz', 'Найденый регион не соответсвует искомому')

    def test_03_country_code_error(self):
        # Проверяем ошибку, если указать неверный код страны
        for i in ('ru', 'kg', 'kz', 'cz'):
            response = get(f'{url}?country_code=ua')
            json_data = response.json()
            self.assertEqual(json_data['items'][0]['country']['code'], i, 'Искомый регион не является '
                                                                          'одним из следующих значений: ru, kg, kz, cz')

    def test_04_unique_page_data(self):
        # Проверяем, что на страницах нет повторяющихся регионов
        page = 1
        item_ids = []
        while True:
            response = get(f'{url}?page={page}')
            json_data = response.json()
            if not json_data['items']:
                break
            for obj in json_data['items']:
                self.assertNotIn(obj['id'], item_ids, 'Повторяющиеся id городов при навигации по страницам')
                item_ids.append(obj['id'])
            page += 1

    def test_05_quantity(self):
        # Проверяем, что количество элементов на странице = 15
        response = get(url)
        json_data = response.json()
        self.assertEqual(len(json_data['items']), 15, 'Количество элементов на странице не равно 15')

    def test_06_total(self):
        # Общее количество уникальных регионов в базе соответствует total
        response = get(url)
        json_data = response.json()
        total = json_data['total']
        page = 1
        items = set()
        while True:
            response = get(f'{url}?page={page}')
            json_data = response.json()
            if not json_data['items']:
                break
            for obj in json_data['items']:
                items.add(obj['id'])
            page += 1
        self.assertEqual(len(items), total, 'Общее количество уникальных регионов в базе не соответствует total')


if __name__ == '__main__':
    main()
