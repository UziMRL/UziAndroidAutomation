import unittest
from appium import webdriver
from selenium.webdriver.common.by import By
import Configuration.ConfigFile

desired_caps = Configuration.ConfigFile.devices_by_ids
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    driver.find_element(By.ID,
                        "com.mobileresearchlabs.asound.q:id/splash_startSpotter").click()
    driver.find_element(By.XPATH,
                        "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout"
                        "/android.widget.LinearLayout/android.widget.FrameLayout["
                        "2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.EditText").send_keys(
                        "101_401_1031")
    driver.find_element(By.ID, "android:id/button1").click()
    driver.implicitly_wait(10)


if __name__ == '__main__':
    unittest.main()
