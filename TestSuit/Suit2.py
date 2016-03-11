import unittest
from common_actions.Actions import CommonActions
from Pages.JqueryDemosPage import JqueryDemos
from Pages.SFdemopage import SFdemoPage
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class Uiops(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        perform = CommonActions(cls)
        cls.browser = perform.open_browser("chrome")

    def setUp(self):
        #self.browser.get('http://jqueryui.com/demos/')
        self.browser.get('http://www.seleniumframework.com/Practiceform/')
        self.browser.implicitly_wait(20)




    def _verify_title(self):
        print(self.browser.title)
        self.assertEqual(self.browser.title, 'jQuery UI Demos | jQuery UI','title did not match')

    def it_demo_page(self):
        JqueryDemos(self.browser).clickonDraggable()
        JqueryDemos(self.browser).basic_ui_ops()

    def _switch_ops(self):

        SFdemoPage(self.browser).switch_actions()

    def test_act2(self):
        SFdemoPage(self.browser).function2()








    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass
        #cls.browser.quit()


if __name__ == '__main__':
    unittest.main()

