from selenium.webdriver.common.by import By
from selenium import webdriver
from common_actions.Actions import CommonActions
import time



class SFdemoPage():

    def __init__(self, browser):
        self.browser = browser#=webdriver.Firefox()

    new_window_button = (By.CSS_SELECTOR, "#button1")
    menu_button = (By.CSS_SELECTOR, "#mobile-menu")
    new_message_window = (By.XPATH, "//button[@onclick='newMsgWin()']")
    message_on_new_window = (By.XPATH, "//*[contains(text()='message']")
    new_browser_tab = (By.XPATH, "//button[@onclick='newBrwTab()']")


    def switch_actions(self):
        """perform switch actions pop up window/modal/alert etc"""
        CommonActions(self.browser).click(self.new_window_button)
        CommonActions(self.browser).switch_to_latest_window()
        CommonActions(self.browser).click(self.menu_button)
        self.browser.close()
        CommonActions(self.browser).switch_to_latest_window()

        CommonActions(self.browser).click(self.new_message_window)
        CommonActions(self.browser).switch_to_latest_window()
        self.browser.maximize_window()
        time.sleep(5)
        #print(CommonActions(self.browser).get_text(self.message_on_new_window))
        print(self.browser.page_source)
        self.browser.close()
        CommonActions(self.browser).switch_to_latest_window()

        print(self.browser.current_url)
        print(self.browser.get_cookies())


