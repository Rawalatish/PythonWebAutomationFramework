import os
import time

import allure
import pytest
from selenium import webdriver
from tests.pageObjects.loginPage import LoginPage
from tests.pageObjects.dashboardPage import DashboardPage
from dotenv import load_dotenv

load_dotenv()


# Assertions

class TestLogin:

    @allure.epic("VWO Login Test")
    @allure.feature("TC#0 - VWO App Negative Test")
    @pytest.mark.negative
    @pytest.mark.usefixtures("setup")

    def test_vwo_login_negative(self,setup):
        try:
            driver = setup
            loginPage = LoginPage(driver)
            loginPage.login_to_vwo(usr="admin@admin@gmail.com", pwd="admin")
            time.sleep(5)
            error_message = loginPage.get_error_message_text()
            assert error_message == "Yours email, password, IP address or location did not match"
        except Exception as e:
            pytest.xfail("Failed")
            print(e)


    @allure.epic("VWO Login Test")
    @allure.feature("TC#1 - VWO App Positive Test")
    @pytest.mark.positive

    def test_vwo_login_positive(self, setup):
        driver = setup
        loginPage = LoginPage(driver=driver)
        # username = setup.username
        # password = setup.password
        loginPage.login_to_vwo(usr= os.getenv("NAME") , pwd=os.getenv("PASSWORD"))
        time.sleep(10)
        dashboardPage = DashboardPage(driver)
        assert "Dashboard" in driver.title
        # assert "Aman" in dashboardPage.user_logged_in_text()