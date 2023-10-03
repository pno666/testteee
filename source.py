from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def find_el(driver, xpath=None, wait_time=10):
    """
    Для более удобного поиска элемента c неявным ожиданием в 10 секунд
    :param wait_time: Время, которое функция будет ожидать элемент
    :param driver: conftest.py
    :param xpath: путь к элементу
    """
    wait = WebDriverWait(driver, wait_time)
    return wait.until(EC.visibility_of_element_located(xpath))
