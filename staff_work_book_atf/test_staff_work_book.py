# -*- coding: utf-8 -*-
"""
Отображение трудовой книжки в карточке сотрудника
https://*****.ru/opendoc.html?*****
Внесение данных заявления на ведение трудовой книжки в карточку сотрудника
https://*****.ru/opendoc.html?*****
"""
from atf import *
from atf.ui import *
from datetime import date
from pages_inside.login import LoginPage
from pages_inside.personnel.index_vdom import Personnel
from pages_inside.personnel.card_staff_new.index import CardStaff
from pages_inside.personnel.card_staff_new.t_pages_work_book import WorkBook
from pages_inside.personnel.personnel_doc.dismiss import DismissForm
from pages_inside.personnel.personnel_doc.transfer import TransferForm
from pages_inside.personnel.personnel_doc.recruit import RecruitForm


class TestStaffWorkBook(TestCaseUI):
    """Тестирование трудовой книжки"""

    staff_name = 'Трудовой Кирилл Олегович'
    staff_f = 'Трудовой'
    staff_nf = 'Трудовой Кирилл'
    dismissal = 'Увольнение'
    transfer = 'Перевод'
    recruit = 'Прием'
    staff_name_2 = 'Трудовая Анастасия Викторовна'
    staff_nf_2 = 'Трудовая Анастасия'
    today_date = date.today().strftime("%d.%m.%y")
    statement = 'электронная'
    statement_no = 'заявление не написано'

    @classmethod
    def setup_class(cls):

        cls.client = LoginPage(cls.driver).login_with_transit(cls.config.USER_NAME, cls.config.PASSWORD, "Сотрудники")

    def setup(self):
        log('Проверяем загрузку реестра, сбрасываем фильтр')
        staff_list = Personnel(self.driver)
        staff_list.personnel_tbl.check_load()
        staff_list.clear_all_filter()

    def test_01_work_book_display(self):
        """Сотрудники. Поиск. Проверка трудовой книжки"""

        log('Ищем сотрудника по ФИО и переходим в карточку')
        staff_list = Personnel(self.driver)
        staff_list.personnel_tbl.check_change(action=lambda: staff_list.search_form.search_inp.type_in(self.staff_name))
        staff_list.personnel_tbl.row(contains_text=self.staff_nf).click()

        log('Переходим в Зарплата и учет/Трудовая книжка')
        page_cs = CardStaff(self.driver)
        page_cs.accordeon_move(top_tab='Зарплата и учет', right_link='Трудовая книжка')

        log('Проверяем отображение кадровых документов: Увольнение, Перевод, Прием')
        page_wb = WorkBook(self.driver)
        page_wb.workbook_list.check_load()
        page_wb.workbook_list.item(contains_text=self.dismissal).should_be(Displayed,
                                                                           msg='Поле увольнения не отображается')
        page_wb.workbook_list.item(contains_text=self.transfer).should_be(Displayed,
                                                                          msg='Поле перевода не отображается')
        page_wb.workbook_list.item(contains_text=self.recruit).should_be(Displayed, msg='Поле приёма не отображается')

        log('Открываем запись об увольнении')
        page_wb.workbook_list.item(contains_text=self.dismissal).click()
        page_dis_form = DismissForm(self.driver)
        page_dis_form.staff_fl.should_be(ExactText(self.staff_name), msg='Документ увольнения не открылся',
                                         wait_time=True)
        page_dis_form.close()

        log('Открываем запись о переводе')
        page_wb.workbook_list.item(contains_text=self.transfer).click()
        page_tr_form = TransferForm(self.driver)
        page_tr_form.staff_fl.should_be(ExactText(self.staff_name), msg='Документ перевода не открылся',
                                        wait_time=True)
        page_tr_form.close()

        log('Открываем запись о приеме')
        page_wb.workbook_list.item(contains_text=self.recruit).click()
        page_rec_form = RecruitForm(self.driver)
        page_rec_form.second_name_inp.should_be(ExactText(self.staff_f), msg='Документ увольнения не открылся',
                                                wait_time=True)
        page_rec_form.close_old_btn.click()

        log('Закрываем карточку сотрудника')
        page_cs.close()

    def test_02_work_book_editing(self):
        """Сотрудники. Поиск. Внесение изменений в трудовую книжку"""

        log('Ищем сотрудника по ФИО и переходим в карточку')
        staff_list = Personnel(self.driver)

        staff_list.personnel_tbl.check_change(
            action=lambda: staff_list.search_form.search_inp.type_in(self.staff_name_2))
        staff_list.personnel_tbl.row(contains_text=self.staff_nf_2).click()

        log('Переходим в Зарплата и учет/Трудовая книжка')
        page_cs = CardStaff(self.driver)
        page_cs.card_staff_form_elm.should_be(ContainsText(self.staff_name_2), wait_time=True,
                                              msg='Карточка сотрудника не отображается')
        page_cs.accordeon_move(top_tab='Зарплата и учет', right_link='Трудовая книжка')

        log('Редактируем карточку сотрудника: выбираем тип Электронная, вводим текущую дату, сохраняем')
        page_cs.open_edit_mode()
        page_wb = WorkBook(self.driver)
        page_wb.statement_lnk.should_be(Displayed, msg='Редактирование заявления не отобразилось').click()
        page_wb.stat_win_elm.should_be(Displayed, msg='Окно выбора заявления не открылось')
        page_wb.statement_dlg.workbook_radio.select(contains_text=self.statement)
        page_wb.statement_dlg.date_cdp.set_date(self.today_date)
        page_wb.statement_dlg.save_btn.should_be(Displayed, msg='Кнопка сохранить не отображается').click()
        page_wb.statement_lnk.should_be(ContainsText(self.statement),
                                        msg='Ссылка-действие не соответсвует типу заявления')
        page_cs.save()

        log('Редактируем карточку сотрудника: выбираем тип Заявление не написано, сохраняем')
        page_cs.open_edit_mode()
        page_wb.statement_lnk.should_be(Displayed, msg='Редактирование заявления не отобразилось').click()
        page_wb.stat_win_elm.should_be(Displayed, msg='Окно выбора заявления не открылось')
        page_wb.statement_dlg.workbook_radio.select(contains_text=self.statement_no)
        page_wb.statement_dlg.save_btn.should_be(Displayed, msg='Кнопка сохранить не отображается').click()
        page_wb.statement_lnk.should_be(ContainsText(self.statement_no),
                                        msg='Ссылка-действие не соответсвует типу заявления')
        page_cs.save()

        log('Закрываем карточку сотрудника')
        CardStaff(self.driver).close()

    def teardown(self):
        self.browser.close_windows_and_alert()


if __name__ == '__main__':
    run_tests()
