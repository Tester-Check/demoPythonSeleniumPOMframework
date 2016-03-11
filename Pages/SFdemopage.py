from selenium.webdriver.common.by import By
from selenium import webdriver
from common_actions.Actions import CommonActions
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
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
    change_color_button = (By.ID, "colorVar")
    draggable = (By.ID, "draga")
    droppable = (By.ID, "dragb")
    text_area =(By.NAME, "vfb-10")
    date_picker =(By.NAME, "vfb-8")
    dropdownbox =(By.NAME, "vfb-12")


    def switch_actions(self):
        browser = self.browser
        first_color = CommonActions(browser).get_attribute(self.change_color_button,'style')
        #CommonActions(browser).click(self.new_message_window)

        """CommonActions(browser).switch_to_latest_window()
        browser.maximize_window()

        #print(CommonActions(browser).get_text(self.message_on_new_window))
        print(browser.page_source)
        browser.close()
        CommonActions(browser).switch_to_latest_window()

        print(browser.current_url)"""
        print(browser.get_cookies())

        CommonActions(browser).click(self.alert_button)

        CommonActions(browser).accept_alert()
        print("--------------------------------------")
        #CommonActions(browser).click(self.timing_alert_button)
        #CommonActions(browser).accept_alert()

        print(first_color)
        CommonActions(browser).click(self.change_color_button)
        print(CommonActions(browser).get_attribute(self.change_color_button,'style'))


        #CommonActions(browser).dragondrop(self.draggable, self.droppable)
        CommonActions(browser).dragon2(self.draggable, self.droppable)
        time.sleep(4)



    def function2(self):
        browser = self.browser
        CommonActions(browser).set_text(self.date_picker, time.strftime("%m/%d/"+"20"+"%y"))
        CommonActions(browser).set_text(self.date_picker,Keys.ENTER)
        CommonActions(browser).select_dropdown_by_value(self.dropdownbox, "Option 2")















