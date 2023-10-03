appium_server_url = 'http://localhost:4723/'

configurations = [
    {
        "platformName": "Android",
        "platformVersion": "13",
        "appium:automationName": "UiAutomator2",
        "appium:deviceName": "emulator-5554",
        "appium:appPackage": "com.taptable",
        "appium:appActivity": "com.taptable.SplashActivity"
    }
]
