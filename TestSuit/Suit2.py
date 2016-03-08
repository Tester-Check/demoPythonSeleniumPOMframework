import unittest
from common_actions.Actions import CommonActions
from Pages.JqueryDemosPage import JqueryDemos
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class Uiops(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        perform = CommonActions(cls)
        cls.browser = perform.open_browser("chromesssdguuu1")

    def setUp(self):
        self.browser.get('http://jqueryui.com/demos/')
        self.browser.implicitly_wait(20)




    def test_verify_title(self):
        print(self.browser.title)
        self.assertEqual(self.browser.title, 'jQuery UI Demos | jQuery UI','title did not match')

    def test_demo_page(self):
        JqueryDemos(self.browser).clickonDraggable()
        JqueryDemos(self.browser).basic_ui_ops()

    def test_switch_ops(self):
        self.browser.get('http://www.seleniumframework.com/Practiceform/')
        






    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()


if __name__ == '__main__':
    unittest.main()

