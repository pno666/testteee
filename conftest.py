import pytest
import os
import subprocess

from datetime import datetime
from appium import webdriver
from constants import appium_server_url, configurations


# Формирование id для каждой конфигурации
def configuration_ids(config):
    return f"{config['platformName']}-{config['platformVersion']}-{config['deviceName']}"


def is_device_available(device_name):
    # Выполнение adb команды для получения списка устройств
    try:
        result = subprocess.check_output(["adb", "devices"]).decode("utf-8")
        # Проверить, содержит ли вывод имя устройства
        return device_name in result
    except subprocess.CalledProcessError:
        return False


# Параметры устройства и запуск.
@pytest.fixture(scope="function", params=configurations, ids=configuration_ids)
def init_appium_driver(request):
    options = request.param
    print(f"Options: {options}")

    if not is_device_available(options['deviceName']):
        pytest.skip(f"Устройство {options['deviceName']} недоступно")

    driver = webdriver.Remote(appium_server_url, options)
    yield driver
    driver.quit()


# Фикстура для инициализации драйвера appium.
@pytest.fixture(scope="function")
def driver(init_appium_driver):
    yield init_appium_driver
