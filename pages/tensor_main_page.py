from .base_page import BasePage
from .locators import TensorMainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TensorMainPage(BasePage):
    def should_be_block_power_in_peoples(self):
        self.browser.execute_script("window.scrollTo(0, 1080)")
        #power_in_peoples_block = WebDriverWait(self.browser, 25).until(EC.visibility_of_element_located(TensorMainPageLocators.POWER_IN_PEOPLE_BLOCK))
        power_in_peoples_block = self.browser.find_element(*TensorMainPageLocators.POWER_IN_PEOPLE_BLOCK)
        assert power_in_peoples_block, 'Block power in peoples should be present'



    
