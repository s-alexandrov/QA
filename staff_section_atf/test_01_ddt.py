from atf import *
from atf.ui import *
from datetime import timedelta, datetime, date
from atf.datageneration import months
from atf.datageneration import add_months

from qa.staff_section_atf.pages.login_01 import LoginPage
from qa.staff_section_atf.pages.profile_01 import ProfilePage


@ddt
class TestTablePage(TestCaseUI):
    """"Тестирование страницы Табели"""

    todayDate = date.today()
    pastDate = (todayDate - timedelta(days=120)).replace(day=todayDate.day)
    futureDate = add_months(tmp_date=todayDate, months_num=15)

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

    @data(todayDate, pastDate, futureDate)
    def test_01_date(self, dates):
        """Проверка фильтрации по месяцу и году"""

        page = ProfilePage(self)

        log("Выставляем дату и проверяем соот-е документов в реестре")
        page.date.open().set_year(year=dates.year).select_mouth(number_mouth=dates.month,
                                                                value="{}{}".format(months[dates.month - 1],
                                                                                    f"'{dates.strftime('%y')}"))
        page.date_tbl.should_be(Displayed, wait_time=True)
        date_list = page.date_tbl.rows_number
        for item in range(1, date_list):
            page.date_tbl.row(row_number=item).should_be(ContainsText(dates.strftime("%m.%y")))


if __name__ == '__main__':
    run_tests()
