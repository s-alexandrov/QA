"""
Тестовое задание для инженера по автоматизированному тестированию ПО. Тест 2.
https://drive.google.com/file/d/1rkO3_C7ZS-dDfRvPOueZ39iArZKIxoaI/view
"""
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class YandexMailLogin(unittest.TestCase):
    """Открываем главную страницу Google, выполняем поиск"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.driver.get('https://google.ru/')

    def test_1_search_site(self):
        # Проверяем, что открылась главная страница.
        driver = self.driver
        self.assertIn('Google', driver.title, msg='Главная страница Google не открылась')

        # Вводим поисковый запрос, выполняем поиск.
        search = self.driver.find_element(By.CSS_SELECTOR, '[name="q"]')
        search.send_keys('купить кофемашину bork c804')
        search.send_keys(Keys.ENTER)

        # Проверяем, что результатов поиска больше 10.
        result = self.driver.find_element(By.CSS_SELECTOR, '.LHJvCe div').text
        result_str = [i for i in result.split() if i.isdigit()]
        x = ''
        for i in result_str:
            x += i
        result_int = int(x)
        assert (result_int > 10)

        # Проверяем, что в результатах поиска присудствует сайт mvideo.ru.
        urls = driver.find_element_by_partial_link_text(link_text='mvideo.ru')
        self.assertIn('mvideo.ru', urls.text, 'Сайт не найден в результатах поиска')


if __name__ == '__main__':
    unittest.main()
