# -*- coding: utf-8 -*-
from atf.ui import *


class YandexSearchLocators(Page):
    """Главная страница Yandex"""

    search_inp           = TextField(    By.ID, 'text', "Строка поиска")
    suggest_slc          = Select(       By.CLASS_NAME, 'mini-suggest__popup-content', "Таблица поисковых подсказок")
    result_cslst         = CustomList(   By.CLASS_NAME, 'link_theme_outer', "Поиск URLa")
    # search_url_lnk       = Link(         By.LINK_TEXT, 'tensor.ru')
