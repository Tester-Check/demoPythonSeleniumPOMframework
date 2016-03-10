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
    alert_button = (By.XPATH, "//button[@onclick='newAlert()']")
    timing_alert_button = (By.ID, "timingAlert")
    change_color_button = (By.ID, "button#colorVar")


    def switch_actions(self):
        browser = self.browser
        CommonActions(browser).click(self.new_message_window)
        CommonActions(browser).switch_to_latest_window()
        browser.maximize_window()
        time.sleep(5)
        #print(CommonActions(browser).get_text(self.message_on_new_window))
        print(browser.page_source)
        browser.close()
        CommonActions(browser).switch_to_latest_window()

        print(browser.current_url)
        print(browser.get_cookies())

        CommonActions(browser).click(self.alert_button)
        CommonActions(browser).accept_alert()
        print("--------------------------------------")
        CommonActions(browser).click(self.timing_alert_button)
        CommonActions(browser).accept_alert()

        print(CommonActions(browser).get_attribute(self.change_color_button,'color'))
        CommonActions(browser).click(self.change_color_button)
        print(CommonActions(browser).get_attribute(self.change_color_button,'color'))











