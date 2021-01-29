"""
Тестовое задание для инженера по автоматизированному тестированию ПО. Тест 1.
https://drive.google.com/file/d/1rkO3_C7ZS-dDfRvPOueZ39iArZKIxoaI/view
"""
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class YandexMailLogin(unittest.TestCase):
    """Открываем главную струницу Яндекса и логинимся в почте"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.driver.get('https://yandex.ru/')

    def test_login_yandex_mail(self):
        # Проверяем, что открылась главная страница. Кликаем по кропке "Войти в почту"
        driver = self.driver
        self.assertIn('Яндекс', driver.title, msg='Открыта не главная страница Яндекс')
        driver.find_element_by_link_text('Войти в почту').click()

        # Переключаемся на новую вкладку, проверяем
        driver.switch_to.window(driver.window_handles[1])
        self.assertIn('Авторизация', driver.title, msg='Страница авторизации не открылась')

        # Вводим логин и пароль. Проверяем, что залогинились
        driver.find_element(By.CSS_SELECTOR, '[name="login"]').send_keys('stesting.ru')
        driver.find_element(By.CSS_SELECTOR, 'button.Button2').click()
        driver.find_element(By.CSS_SELECTOR, '[name="passwd"]').send_keys('p1234567')
        driver.find_element(By.CSS_SELECTOR, '.Button2_view_action').click()
        time.sleep(1)
        self.assertIn('Яндекс.Почта', driver.title, msg='Не перешли в почту. Могла открыться форма ввода моб.телефона')


if __name__ == '__main__':
    unittest.main()
