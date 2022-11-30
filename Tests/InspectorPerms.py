import unittest
from appium import webdriver
from selenium.webdriver.common.by import By
import Configuration.ConfigFile
from appium.webdriver.common.appiumby import AppiumBy

from test100 import el4

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
    el4 = driver.find_element(by=AppiumBy.ID, value="com.mobileresearchlabs.asound.q:id/splash_startButton")
el4.click()
el5 = driver.find_element(by=AppiumBy.ID, value="com.mobileresearchlabs.asound.q:id/splash_startButton")
el5.click()
el6 = driver.find_element(by=AppiumBy.ID, value="com.mobileresearchlabs.asound.q:id/splash_startButton")
el6.click()
el7 = driver.find_element(by=AppiumBy.ID, value="com.android.permissioncontroller:id/permission_allow_foreground_only_button")
el7.click()
el8 = driver.find_element(by=AppiumBy.ID, value="com.android.permissioncontroller:id/permission_allow_foreground_only_button")
el8.click()
el9 = driver.find_element(by=AppiumBy.ID, value="android:id/button1")
el9.click()
el10 = driver.find_element(by=AppiumBy.ID, value="com.android.permissioncontroller:id/allow_always_radio_button")
el10.click()
el11 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Back")
el11.click()
el12 = driver.find_element(by=AppiumBy.ID, value="com.android.permissioncontroller:id/permission_allow_button")
el12.click()
el13 = driver.find_element(by=AppiumBy.ID, value="com.android.permissioncontroller:id/permission_allow_button")
el13.click()
el14 = driver.find_element(by=AppiumBy.ID, value="com.android.permissioncontroller:id/permission_allow_button")
el14.click()
el15 = driver.find_element(by=AppiumBy.ID, value="com.mobileresearchlabs.asound.q:id/splash_startButton")
el15.click()
el16 = driver.find_element(by=AppiumBy.ID, value="android:id/button1")
el16.click()
el17 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.LinearLayout[2]")
el17.click()
el18 = driver.find_element(by=AppiumBy.ID, value="android:id/switch_widget")
el18.click()
el19 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Navigate up")
el19.click()
el20 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Navigate up")
el20.click()
el21 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.LinearLayout[2]")
el21.click()
el22 = driver.find_element(by=AppiumBy.ID, value="android:id/switch_widget")
el22.click()
el23 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Navigate up")
el23.click()
el24 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[7]/android.widget.LinearLayout[2]")
el24.click()
el25 = driver.find_element(by=AppiumBy.ID, value="android:id/switch_widget")
el25.click()
el26 = driver.find_element(by=AppiumBy.ID, value="com.android.settings:id/allow_button")
el26.click()
el27 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Navigate up")
el27.click()



if __name__ == '__main__':
    unittest.main()
