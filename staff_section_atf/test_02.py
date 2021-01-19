from atf import *
from atf.ui import *
from datetime import date

from qa.staff_section_atf.pages.login_02 import LoginPage
from qa.staff_section_atf.pages.profile_02 import ProfilePage


class TestTablePage(TestCaseUI):
    """"Тестирование страницы Совещания"""

    @classmethod
    def setup_class(cls):

        cls.browser.open(cls.config.get('SITE') + 'events')
        login_page = LoginPage(cls)
        login_page.login_as("*****", "*****")

    def setup(self):
        page = ProfilePage(self)
        page.navigation_contacts_cslst.item(contains_text='Контакты').should_be(Displayed,
                                                                                msg='Раздел Контакты не отобразился')
    def test_01(self):

        log("Создаем новое совещание и проверяем, что оно отобразилось в реестре")
        page = ProfilePage(self)
        page.event_btn.should_be(Displayed, wait_time=True, msg='Кнопка Событие не отобразалась').click()
        page.meeting_cslst.should_be(Displayed, wait_time=True, msg='Меню Совещание не отобразалось').item(
            contains_text='Совещание').click()
        page.when_lnk.should_be(Displayed, wait_time=True, msg='Совещание не отобразилось').click()
        page.calendar_elm.should_be(Displayed, wait_time=True, msg='Календарь не отобразился')
        page.calendar_close_btn.click()
        today = date.today().strftime("%d")
        assert_that(today, is_in(page.date_elm.text), 'Установленная дата не совпала')
        page.date_inp.type_in(string='15:30', clear_txt=True)
        description = 'Новая задача'
        page.description_cta.should_be(Displayed, wait_time=True, msg='Поле не отобразилось').type_in(
            string=description, clear_txt=True)
        page.start_btn.should_be(Displayed, wait_time=True).click()
        assert_that(description, is_in(page.reestr_cslst.item(with_text=description).text), 'Совещание не отображается')


if __name__ == '__main__':
    run_tests()
