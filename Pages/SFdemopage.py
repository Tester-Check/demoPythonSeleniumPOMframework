from selenium.webdriver.common.by import By
from selenium import webdriver
from common_actions.Actions import CommonActions



class SFdemoPage():

    def __init__(self, browser):
        self.browser = browser#=webdriver.Firefox()

    new_window_button = (By.CSS_SELECTOR, "#button1")
    menu_button = (By.CSS_SELECTOR, "#mobile-menu")


    def switch_actions(self):
        """perform switch actions window/modal/alert"
        CommonActions(self.browser).click(SFdemoPage.new_window_button)
        CommonActions(self.browser).switch_to_latest_window()
        CommonActions(self.browser).click(SFdemoPage.menu_button)

