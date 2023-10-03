import pytest
from locators import LoginPageLocators
from source import find_el


def test_open_app(driver):
    btn_login = find_el(driver, LoginPageLocators.LOGIN_BTN)
    assert btn_login.is_displayed(), "raratata"
