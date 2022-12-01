import unittest
from appium import webdriver
from selenium.webdriver.common.by import By
import Configuration.ConfigFile
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

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
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.mobileresearchlabs.asound.q:id/splash_startSpotter")))


driver.find_element(By.ID, "com.mobileresearchlabs.asound.q:id/splash_startSpotter").click()
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "com.mobileresearchlabs.asound.q:id/splash_startButton")))
time.sleep(3)

driver.find_element(By.ID, "com.mobileresearchlabs.asound.q:id/splash_startButton").click()
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "com.mobileresearchlabs.asound.q:id/splash_startButton")))
driver.find_element(By.ID, "com.mobileresearchlabs.asound.q:id/splash_startButton").click()
driver.find_element(By.ID, "com.mobileresearchlabs.asound.q:id/splash_startButton").click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located(
    (By.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button")))
driver.find_element(By.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button").click()
time.sleep(2)
driver.find_element(By.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button").click()
time.sleep(2)
driver.find_element(By.ID, "android:id/button1").click()

driver.find_element(By.ID, "com.android.permissioncontroller:id/allow_always_radio_button").click()
time.sleep(2)
driver.find_element(By.XPATH, '//android.widget.ImageButton[@content-desc="Back"]').click()
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "com.android.permissioncontroller:id/permission_allow_button")))
driver.find_element(By.ID, "com.android.permissioncontroller:id/permission_allow_button").click()
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "com.android.permissioncontroller:id/permission_allow_button")))
driver.find_element(By.ID, "com.android.permissioncontroller:id/permission_allow_button").click()
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "com.android.permissioncontroller:id/permission_allow_button")))
driver.find_element(By.ID, "com.android.permissioncontroller:id/permission_allow_button").click()
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "com.mobileresearchlabs.asound.q:id/splash_startButton")))
time.sleep(5)
driver.quit()

if __name__ == '__main__':
    unittest.main()
