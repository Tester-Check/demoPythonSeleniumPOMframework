
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common import by
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from Utilities.excel_actions import excel_utils


class CommonActions(object):
    def __init__(self, browser):
        #browser =webdriver.Firefox()
        self.browser = browser


    def open_browser(self, browser_name):
        if(browser_name == "chrome"):
            self.browser = webdriver.Chrome('/Users/shreyas/Documents/chromedriver')
        elif(browser_name == "ff"):
            self.browser = webdriver.Firefox()

        self.browser.maximize_window()
        return self.browser

    def click(self, web_element):
        #ele = self.browser.find_element(by=web_element[0], value=web_element[1])
        element = WebDriverWait(self.browser, 10).until(expected_conditions.element_to_be_clickable(web_element))
        #WebDriverWait(self.browser).until(lambda s: s.find_element(by=web_element[0], value=web_element[1]))
        element.click()





    def set_text(self, locator, text):
        element = WebDriverWait(self.browser, 10).until(expected_conditions.presence_of_element_located(locator))
        #browser.find_element_by_xpath("//*[@id='user_login']").send_keys('soorajh4@gmail.com')
        element.send_keys(text)

    def get_text(self, locator):
        element = WebDriverWait(self.browser, 10).until(expected_conditions.visibility_of_element_located(locator))
        return element.text

    def get_list(self, locator):
        elements = WebDriverWait(self.browser, 10).until(expected_conditions.presence_of_all_elements_located(locator))
        list_contents=[]
        for element in elements:
            list_contents.append(element.text)
        return list_contents


    def accept_alert(self): #acceps alert
        #WebDriverWait(self.browser, 10).until(expected_conditions.alert_is_present, message="looking for alert")
        self.browser.switch_to.alert.accept()

    def switch_to_latest_window(self):
        """switches to latest window"""
        browser = self.browser
        browser.switch_to.window(browser.window_handles[-1])

    def switch_to_frame(self, frame_ref):
        """switches to frame by id,name /web element """
        self.browser.switch_to.frame(frame_reference=frame_ref)

    def read_from_excel(self, filepath, sheetindex, rownum, colnum):
        excel_utils.read_cell(filepath, sheetindex, rownum, colnum)

    def select_dropdown_by_value(self, locator, value):
        """selects dropdown option by value"""
        element = WebDriverWait(self.browser, 10).until(expected_conditions.visibility_of_element_located(locator))
        select = Select(element)
        select.select_by_value(value)

    def get_attribute(self, locator, attr):
        element = WebDriverWait(self.browser, 10).until(expected_conditions.presence_of_element_located(locator))
        return self.browser.find_element(element).get_attribute(attr)

    def wait_for_visibliity(self, locator, attr):
        element = WebDriverWait(self.browser, 10).until(expected_conditions.visibility_of_element_located(locator))







    




