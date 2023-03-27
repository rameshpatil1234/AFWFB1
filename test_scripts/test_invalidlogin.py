from generic.base_test import BaseTest
from generic.utility import Excel
from pages.loginpage import LoginPage


class Test_InValidLogin(BaseTest):

    def test_invalidlogin(self):
        un = Excel.get_cell_value("../data/input.xlsx", "Invalidlogin", 2, 1)
        pw = Excel.get_cell_value("../data/input.xlsx", "Invalidlogin", 2, 2)
        loginpage =LoginPage(self.driver)
        loginpage.set_username(un)
        loginpage.set_password(pw)
        loginpage.click_on_loginbutton()
        result = loginpage.verify_err_msg_is_displayed(self.wait)
        assert result

