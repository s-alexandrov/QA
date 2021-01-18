# -*- coding: utf-8 -*-
from atf.ui import *


class YandexImagesLocators(Page):
    """Взаимодействие с элементами страницы Яндекс.Картинки"""

    image_lnk                      = Link(         By.LINK_TEXT, 'Картинки', "Ссылка Картинки")
    image_category_cslst           = CustomList(   By.CLASS_NAME, 'PopularRequestList-Preview', "Категории Картинок")
    image_cslst                    = CustomList(   By.CLASS_NAME, 'serp-item__link', "Коллекция Картинок")
    image_next_elm                 = Element(      By.CLASS_NAME, 'MediaViewer_theme_fiji-ButtonNext', "Следующая картинка")
    image_previous_elm             = Element(      By.CLASS_NAME, 'MediaViewer_theme_fiji-ButtonPrev', "Предыдущая картинка")