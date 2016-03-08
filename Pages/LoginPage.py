from common_actions.Actions import CommonActions
from selenium import  webdriver
from selenium.webdriver.common.by import By


class LoginPageClass(object):
    #myprofilename = 'h2.profile-gravatar__user-display-name'
    profile_name = (By.CSS_SELECTOR, 'h2.profile-gravatar__user-display-name')

    #pn =
    #profile_name = lambda self: self.webdriver.find_element_by_css_selector('h2.profile-gravatar__user-display-name')
    def __init__(self,browser):
        self.browser = browser

    def profile_name(self):
        profile_name =self.browser.find_element_by_css_selector('h2.profile-gravatar__user-display-name')
        return profile_name




    def loginToWordpress(self):
        browser = self.browser
        CommonActions(browser).set_text()

        #browser.find_element_by_xpath("//*[@id='user_login']").send_keys('soorajh4@gmail.com')
        browser.find_element_by_name('pwd').send_keys('srj1srj2srj')
        browser.find_element_by_xpath("//*[@name='wp-submit']").submit()
        #qwwee




