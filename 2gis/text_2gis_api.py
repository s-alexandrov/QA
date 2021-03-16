"""
Тестовое задание 2ГИС на вакансию QA-инженер
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

    def test_02_total(self):
        # Проверяем количество регионов в базе
        response = get(url)
        json_data = response.json()
        self.assertEqual(json_data['total'], 22)

    def test_03_region_search(self):
        # Проверяем поиск региона
        response = get(f'{url}?q=рск')
        json_data = response.json()
        self.assertEqual(len(json_data['items']), 5)
        self.assertEqual(json_data['items'][2]['name'], 'Новосибирск')

        # Проверяем, что country_code игнорируется и количество записей не меняется
        response = get(f'{url}?q=рск&country_code=cz')
        json_data = response.json()
        self.assertEqual(len(json_data['items']), 5)

    def test_04_region_search_empty(self):
        # Проверяем, что поиск несуществующего региона выдает пустой список
        response = get(f'{url}?q=hdfhrehgreh')
        json_data = response.json()
        self.assertEqual(len(json_data['items']), 0)

    def test_05_region_search_error(self):
        # Проверяем на наличие ошибки, если q меньше 3-х символов
        response = get(f'{url}?q=ск')
        json_data = response.json()
        self.assertEqual(json_data['error']['message'], "Параметр 'q' должен быть не менее 3 символов")

    def test_06_country_code_search(self):
        # Проверяем фильтрацию по коду страны
        response = get(f'{url}?country_code=cz')
        json_data = response.json()
        self.assertEqual(len(json_data['items']), 1)
        self.assertEqual(json_data['items'][0]['country']['code'], 'cz')

    def test_07_country_code_error(self):
        # Проверяем ошибку, если указать неверный код страны
        response = get(f'{url}?country_code=us')
        json_data = response.json()
        self.assertEqual(json_data['error']['message'], "Параметр 'country_code' может быть одним из следующих "
                                                        "значений: ru, kg, kz, cz")

    def test_08_page_size(self):
        # Проверяем, что Количество элементов на странице = 5, 10 или 15
        for i in (5, 10, 15):
            response = get(f'{url}?page_size={i}')
            json_data = response.json()
            self.assertEqual(len(json_data['items']), i)

    def test_09_page_size_error(self):
        # Провем ошибку, если указать неверное количество элементров на странице
        response = get(f'{url}?page_size=3')
        json_data = response.json()
        self.assertEqual(json_data['error']['message'], "Параметр 'page_size' может быть одним из следующих "
                                                        "значений: 5, 10, 15")

    def test_10_page_inequality(self):
        # Проверяем, что данные на двух страницах отличаются
        response_1 = get(f'{url}?page=1')
        json_data_1 = response_1.json()
        response_2 = get(f'{url}?page=2')
        json_data_2 = response_2.json()
        self.assertNotEqual(json_data_1['items'], json_data_2['items'])


if __name__ == '__main__':
    main()
