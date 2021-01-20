# -*- coding: utf-8 -*-
"""
Кадровый учет
https://*****.ru/opendoc.html?guid=12194324-8a35-49aa-8884-4b09e80038ed
"""
from atf import *
from atf.ui import *
from pages_inside.login import LoginPage
from pages_inside.personnel.personnel_doc.index import PersonnelDoc
from pages_inside.personnel.personnel_doc.page_indexation import PagePersonnelAccounting
from pages_inside.personnel.index import Position


class PersonnelAccounting(TestCaseUI):
    """Тестирование Кадровый учет"""

    org_name = 'АВТОТЕСТИРОВАНИЕ - НЕ ТРОГАТЬ!'
    date = '25.02.21'
    position = 'ВУТ'
    staff = 'Smoke ИзменениеКлассаУсловий Петрович'

    @classmethod
    def setup_class(cls):
        cls.client = LoginPage(cls.driver).login_with_transit(cls.config.USER_NAME, cls.config.PASSWORD, "Сотрудники",
                                                              "Кадровый учет")

    def setup(self):
        page_pd = PersonnelDoc(self.driver)
        page_pd.wait_for_load(org_name=self.org_name)

    def test_01_create_reception(self):
        """Сотрудники/Кадровый учет. Изменение класса условий"""

        log('Открываем изменение класса условий')
        page_pd = PersonnelDoc(self.driver)
        page_pd.open_new_doc_form('Изменение класса условий')

        log('Вводим дату изменения')
        page_wb = PagePersonnelAccounting(self.driver)
        page_wb.check_open()
        page_wb.date_dp.set_date(date_str=self.date)

        log('Ввыбираем должность')
        page_wb.position_clg.click()
        select_ps = Position(self.driver)
        select_ps.change_position_tab(position=self.position)

        log('Проверяем отображение условий и сотрудникок выбраной должности')
        page_wb.condition_elm.should_be(ContainsText('Оклад'), wait_time=True, msg='Поле оклад не отображается')
        page_wb.staff_clg.should_be(ContainsText(self.staff), msg='Сотрудник не отображается')

        log('Сохраняем условие')
        page_wb.save()


if __name__ == '__main__':
    run_tests()
