# -*- coding: utf-8 -*-
from atf.ui import *


@templatename('Cadres/documents:Indexation')
class PagePersonnelAccounting(StackTemplate):
    """Диалог изменения класса условий"""

    date_dp = VDOMControlsDatePicker(By.CSS_SELECTOR, '.controls-Input-DatePicker', 'Дата')
    condition_elm = Element(By.CSS_SELECTOR, '.cadres-accruals-list', 'Поле условий')
    staff_clg = VDOMControlsListGrid(By.CSS_SELECTOR, '[name="content"] [name="content"] .controls-Grid', 'Описание')
    position_clg = VDOMControlsLookup(By.CSS_SELECTOR, '.staffPost-Choice__lookup', 'Описание')
