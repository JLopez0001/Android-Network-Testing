from appium import webdriver
from appium.options.android import UiAutomator2Options

appium_server_url = 'http://localhost:4723'
device_serial_number = '1A261JEG502007'

def get_driver():
    capabilities = {
        'platformName': 'Android',
        'automationName': 'UiAutomator2',
        'deviceName':device_serial_number,
        "appPackage": "com.google.android.youtube",
        'appActivity': 'com.google.android.apps.youtube.app.WatchWhileActivity', 
        'noReset': True
    }

    driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
    return driver