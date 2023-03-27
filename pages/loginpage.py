from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    __unTB = (By.ID, "email")
    __pwTB = (By.ID, "pass")
    __loginBTN = (By.NAME, "login")
    __errMSG = (By.XPATH, "//div[contains(text(),'incorrect')]")

    def __init__(self,driver):
        self.__driver = driver

    def set_username(self,un):
        self.__driver.find_element(*self.__unTB).send_keys(un)

    def set_password(self,pw):
        self.__driver.find_element(*self.__pwTB).send_keys(pw)

    def click_on_loginbutton(self):
        self.__driver.find_element(*self.__loginBTN).click()

    def verify_err_msg_is_displayed(self,wait):
        try:
            result = wait.until(EC.visibility_of_element_located(self.__errMSG))
            print("Error msg is displayed")
            return True
        except:
            print("Error msg is not displayed")
            return False
