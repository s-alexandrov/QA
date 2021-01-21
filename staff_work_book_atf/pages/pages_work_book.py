# -*- coding: utf-8 -*-
from atf.ui import *


@templatename('EmployeeAccounting/_employmentHistory/BookType/Dialog')
class WorkBookStatement(Region):
    """Диалог выбора типа заявления"""

    workbook_radio     = VDOMControlsToggleRadio( By.CSS_SELECTOR,
                                                  '.controls-RadioGroup__wrapper_vertical', 'Выбор заявления')
    date_cdp           = VDOMControlsDatePicker(  By.CSS_SELECTOR, '.controls-Input-DatePicker', 'Ввод даты')
    save_btn           = Button(                  By.CSS_SELECTOR, '.icon-Yes',
                                                  'Сохранить всплывашку карточки сотрудника')


class WorkBook(Region):
    """Зарплата и Учет/Трудовая книжка - /staff/"""

    workbook_list      = VDOMControlsList()
    statement_lnk      = Link(                    By.CSS_SELECTOR, '.employeeAccounting-TypeEmploymentRecordBook__button',
                                                  'Заявление')
    stat_win_elm       = Element(                 By.CSS_SELECTOR,
                                                  '[template="EmployeeAccounting/_employmentHistory/BookType/Dialog"]',
                                                  'Окно выбора заявления')
    statement_dlg   =  WorkBookStatement()
