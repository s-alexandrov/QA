# -*- coding: utf-8 -*-
from atf import *
from atf.ui import *
from qa.yandex_atf.pages.images_page import YandexImagesLocators


class YandexImages(TestCaseUI):
    """Тестирование страницы Яндекс.Картинки"""

    def setup(self):
        self.browser.open('https://yandex.ru/')

    def test_01_yandex_images(self):
        """Проверка наличия ссылки Картинки на главной странице"""
        page = YandexImagesLocators(self)
        page.image_lnk.should_be(Displayed, msg='Ссылка Картинки не присутствует на странице')
        page.image_lnk.click()
        page.browser.switch_to_window(1)

        """Проверка, что перешли на url https://yandex.ru/images/ после нажатия ссылки Картинки"""
        page.browser.should_be(UrlContains('https://yandex.ru/images/'))

        """Открытие первой категории"""
        page.image_category_cslst.item(item_number=1).click()

        """Открытие первой картинки"""
        page.image_cslst.item(item_number=1).click()
        delay(0.1)
        url_image = page.browser.current_url
        # print(url_image)

        """Проверка, что картинка открылась"""
        page.image_cslst.should_be(Displayed, msg='Картинка не открылась')

        """Открытие следующей картинки"""
        page.image_next_elm.click()

        """Открытие предыдующей(первой) картинки"""
        page.image_previous_elm.click()
        self.browser.should_be(UrlExact(url_image), msg='URL не совпал с первой картинкой')


if __name__ == '__main__':
    run_tests()
