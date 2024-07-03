from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import keyboard


class classstart:
    def join(self, meeting_link):
        self.driver = webdriver.Chrome(
            "C:\Program Files (x86)\chromedriver.exe")
        self.driver.get(https://us05web.zoom.us/j/7110353028?pwd=M3VMWVFzNEcwUXNDb0FkMEttL0VRQT09
)
        time.sleep(2)
        keyboard.send("tab", do_press=True, do_release=True)
        keyboard.send("tab", do_press=True, do_release=True)
        keyboard.send("enter", do_press=True, do_release=True)
        time.sleep(5)

        self.driver.close()
