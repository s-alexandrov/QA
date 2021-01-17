# -*- coding: utf-8 -*-
from atf import *
from atf.ui import *
from qa.yandex_atf.pages.search_page import YandexSearchLocators


class YandexSearch(TestCaseUI):
    """Тестирование наличия ссылки на сайт tensor.ru при поиске по ключевой фразе Тензор"""

    def setup(self):
        self.browser.open('https://yandex.ru/')

    def test_01_yandex_search(self):
        """Проверка наличия поля поиска"""
        page = YandexSearchLocators(self)
        page.search_inp.should_be(Displayed, msg='Поле поиска не отображается')

        """Ввод поискового запроса"""
        page.search_inp.type_in('Тензор')

        """Проверка наличия таблицы с подсказками (suggest)"""
        page.suggest_slc.should_be(Displayed, msg='Таблица поисковых подсказок не отображается')
        page.search_inp.send_keys(Keys.ENTER)

        """Проверка наличия ссылка на tensor.ru"""
        url = page.result_cslst
        for item in range(1, 6):
            assert_that('https://tensor.ru/', is_in(url.item(item_number=1).get_attribute('href')),
                        'Cсылка на tensor.ru отсутствует в первых 5 результатах')


if __name__ == '__main__':
    run_tests()
