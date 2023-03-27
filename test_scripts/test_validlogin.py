import openpyxl
import pytest

from generic.utility import Excel
from generic.base_test import BaseTest
from pages.loginpage import LoginPage
from pages.homepage import HomePage


class Test_ValidLogin(BaseTest):
    @pytest.mark.run(order=1)
    def test_validlogin(self):
        try:
            un = Excel.get_cell_value("../data/input.xlsx", "Validlogin", 2, 1)
            pw = Excel.get_cell_value("../data/input.xlsx", "Validlogin", 2, 2)
        except:
            un = Excel.get_cell_value("data/input.xlsx", "Validlogin", 2, 1)
            pw = Excel.get_cell_value("data/input.xlsx", "Validlogin", 2, 2)
        loginpage = LoginPage(self.driver)
        loginpage.set_username(un)
        loginpage.set_password(pw)
        loginpage.click_on_loginbutton()
        homepage = HomePage(self.driver)
        result = homepage.verify_homepage_is_displayed(self.wait)
        assert result
