# -*- coding: utf-8 -*-
from atf.ui import *


class ProfilePage(Page):
    """Табели - /tableregistry.html"""
    navigation_staff_cslst    = CustomList(                 By.CSS_SELECTOR, '[name="item-staff"]', 'Сотрудники')
    table_time_tbl            = Table(                      By.CSS_SELECTOR,
                                                            '[data-component="SBIS3.CONTROLS/ScrollContainer"]',
                                                            'Рабочее время')
    navigation_table_cslst    = CustomList(                 By.CSS_SELECTOR,
                    '.controls-Scroll-Container.controls-Scroll.NavigationPanels-SubMenu__scroll.ws-flex-shrink-1',
                                                            'Табели')
    tabs                      = ControlTabButtons(          By.CSS_SELECTOR,
                                                            '[data-component="SBIS3.CONTROLS/Tab/Buttons"]', 'Вкладки')
    date                      = ControlsDateRangeSlider(    By.CSS_SELECTOR,
                    '.controls-Browser__table-fullFilterBlock [data-component="SBIS3.CONTROLS/Date/RangeSlider"]',
                                                            'Дата')
    date_tbl                  = Table(                      By.CSS_SELECTOR,
                    '[data-component="SBIS3.CONTROLS/DataGridView"].wtm__docsRegistryContent_tableDocs_bottom table',
                                                            'Проверка даты')
