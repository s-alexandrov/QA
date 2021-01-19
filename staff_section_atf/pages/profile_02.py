# -*- coding: utf-8 -*-
from atf.ui import *


class ProfilePage(Page):
    """Табели - /tableregistry.html"""
    navigation_contacts_cslst = CustomList(         By.CSS_SELECTOR, '[name="item-contacts"]', 'Контакты')
    navigation_events_cslst   = CustomList(         By.CSS_SELECTOR,
                                '[template="NavigationPanels/_accordion/SubMenu"] .NavigationPanels-SubMenu__menuTitle',
                                                    'События')
    event_btn                 = Button(             By.CSS_SELECTOR, '.mainArea-Toolbar__wrapper .controls-MenuButton',
                                                    'Событие')
    meeting_cslst             = CustomList(         By.CSS_SELECTOR,
                                                    '[template="Controls/menu:Popup"] .controls-Menu__content-wrapper',
                                                    'Совещание')
    when_lnk                  = Link(               By.CSS_SELECTOR, '[sbisname="When"]', 'Когда')
    calendar_elm              = Element(            By.CSS_SELECTOR, '[template="CoreUserCalendar/pages:Stack"]',
                                                    'Календарь')
    calendar_close_btn        = Button(             By.CSS_SELECTOR, '.controls-StackTemplate__command_buttons',
                                                    'Закрыть')
    date_elm                  = Element(            By.CSS_SELECTOR,
                                                    '.events-MeetingCardDateInfoDateStart__dateShort-str',
                                                    'Проверка даты')
    date_inp                  = TextField(          By.CSS_SELECTOR, '[sbisname="TimeStart"] .controls-TextBox__field',
                                                    'Время')
    description_cta           = ControlTextArea(    By.CSS_SELECTOR, '[sbisname="TextArea"]', 'Описание')
    start_btn                 = Button(             By.CSS_SELECTOR, '[sbisname="StartBtn"]', 'Сохранить')
    reestr_cslst              = CustomList(         By.CSS_SELECTOR, '.webinars-MiniCard__title', 'Реестр')
