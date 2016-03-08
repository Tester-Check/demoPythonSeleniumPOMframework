from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from common_actions.Actions import CommonActions

from Pages.LoginPage import LoginPageClass

class VitalFunctionalities(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome('/Users/shreyas/Documents/chromedriver')
        cls.browser.implicitly_wait(15)

    def setUp(self):
        browser = self.browser
        self.browser.get('https://wordpress.com/wp-login.php')
        login = LoginPageClass(self.browser)
        login.loginToWordpress()
        browser.get('https://wordpress.com/me')


        #prof_name = CommonActions(browser).get_text(LoginPageClass.myprofilename)
        prof_name = LoginPageClass(browser).profile_name().text

        print(prof_name)
        self.assertEqual(prof_name,'soorajh','profile name did not match')



    def testverify_page(self):
        pass

        


    def tearDown(self):
        print('ending '+self.browser.name+"'s session")
        #self.browser.quit()


    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)




