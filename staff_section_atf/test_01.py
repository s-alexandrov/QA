from atf import *
from atf.ui import *
from datetime import date, timedelta, datetime

from qa.staff_section_atf.pages.login_01 import LoginPage
from qa.staff_section_atf.pages.profile_01 import ProfilePage


class TestTablePage(TestCaseUI):
    """"Тестирование страницы Табели"""

    @classmethod
    def setup_class(cls):

        cls.browser.open(cls.config.get('SITE') + 'tableregistry.html')
        login_page = LoginPage(cls)
        login_page.login_as("*****", "*****")

        page = ProfilePage(cls)
        page.table_time_tbl.should_be(Displayed, wait_time=True)
        page.tabs.select(contains_text='Документы')

    def setup(self):
        page = ProfilePage(self)
        page.tabs.should_be(Displayed, wait_time=True)

    def test_01_date_today(self):
        """Проверка фильтрации по месяцу и году"""

        page = ProfilePage(self)

        today = datetime.now()
        mouth = today.month
        year = today.year
        today_y = datetime.now().strftime("%y")
        months = {'01': "Январь'",
                  '02': "Февраль'",
                  '03': "Март'",
                  '04': "Апрель'",
                  '05': "Май'",
                  '06': "Июнь'",
                  '07': "Июль'",
                  '08': "Август'",
                  '09': "Сентябрь'",
                  '10': "Октябрь'",
                  '11': "Ноябрь'",
                  '12': f"Декабрь'"}
        log("Выставляем дату и проверяем соот-е документов в реестре")
        page.date.open().set_year(year=year).select_mouth(number_mouth=mouth, value=months[str(mouth)] + today_y)
        page.date_tbl.should_be(Displayed, wait_time=True)
        date_list = page.date_tbl.rows_number
        for item in range(1, date_list):
            page.date_tbl.row(row_number=item).should_be(ContainsText(today.strftime("%m.%y")))

    def test_02_minus_4_months(self):
        """Проверка фильтрации по месяцу и году"""

        page = ProfilePage(self)

        log("Выставляем дату -4 месяц и проверяем соот-е документов в реестре")
        page.date.open().set_year(year=2020).select_mouth(number_mouth=8, value="Август'20")
        page.date_tbl.should_be(Displayed, wait_time=True)
        today = (date.today() - timedelta(days=120)).strftime("%m.%y")
        date_list = page.date_tbl.rows_number
        for item in range(1, date_list):
            page.date_tbl.row(row_number=item).should_be(ContainsText(today))

    def test_03_plus_1_year_3_months(self):
        """Проверка фильтрации по месяцу и году"""

        page = ProfilePage(self)

        log("Выставляем дату +1 год 3 месяца и проверяем соот-е документов в реестре")
        page.date.open().set_year(year=2022).select_mouth(number_mouth=3, value="Март'22")
        page.date_tbl.should_be(Displayed, wait_time=True)
        today = datetime.now()
        years = 1
        months = 3
        current_date = (today + timedelta(days=(years * 360) + (months * 30))).strftime("%m.%y")
        date_list = page.date_tbl.rows_number
        for item in range(1, date_list):
            page.date_tbl.row(row_number=item).should_be(ContainsText(current_date))


if __name__ == '__main__':
    run_tests()
