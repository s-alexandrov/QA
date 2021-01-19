# -*- coding: utf-8 -*-
from atf.ui import *
from atf import *


class LoginPage(Page):
    """Авторизация"""

    login_inp          =    TextField(   By.CSS_SELECTOR, '[name="login"]', "Логин")
    password_inp       =    TextField(   By.CSS_SELECTOR, '[name="password"]', "Пароль")
    login_btn          =    Button(      By.CLASS_NAME, 'auth-Form__submit', "Войти")

    def login_as(self, username, password):
        """Авторизация на странице /auth по логину и паролю"""

        delay(0.5)
        self.login_inp.type_in(username)
        self.password_inp.type_in(password)
        self.login_btn.click()
        self.login_btn.should_be(Hidden, wait_time=True)
        log("Авторизовались")
