from selenium.webdriver.common.by import By
from common_actions.Actions import CommonActions
from selenium.webdriver.common.keys import Keys

class JqueryDemos():

    def __init__(self, browser):
        self.browser = browser


    Draggable_link= (By.XPATH, "//a[text()='Draggable']")
    Search_field= (By.CSS_SELECTOR, "input[placeholder='Search']")
    search_result= (By.CSS_SELECTOR, "a[title*='Slider']")
    search_button = (By.CSS_SELECTOR, ".icon-search")
    menu_items = (By.CSS_SELECTOR, ".menu-item>a")

    def clickonDraggable(self):
        CommonActions(self.browser).click(JqueryDemos.Draggable_link)


    def search_for_item(self):
        CommonActions(self.browser).set_text(JqueryDemos.Search_field, 'Slider')
        CommonActions(self.browser).click(JqueryDemos.search_button)
        #self.browser.find_element(JqueryDemos.Search_field).send_keys(Keys.ENTER)
        print(CommonActions(self.browser).get_text(JqueryDemos.search_result))
        print(CommonActions(self.browser).get_list(JqueryDemos.menu_items))
