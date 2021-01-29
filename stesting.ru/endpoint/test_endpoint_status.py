"""
Тестовое задание для инженера по автоматизированному тестированию ПО. Тест 3.
https://drive.google.com/file/d/1rkO3_C7ZS-dDfRvPOueZ39iArZKIxoaI/view
"""
import requests
from unittest import TestCase, main


class TestEndpoint(TestCase):

    def test_endpoint_200(self):
        response = requests.get('https://reqres.in/api/single_user')
        self.assertEqual(200, response.status_code, "Ответ сервера не равен 200")

        response_name = response.json()
        self.assertIn("first_name", response_name, "Ключ first_name не найден")
        self.assertEqual(response_name["first_name"], "Janet", "Ключ first_name не соответсвует Janet")


if __name__ == '__main__':
    main()