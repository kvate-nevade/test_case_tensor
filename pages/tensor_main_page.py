from .base_page import BasePage
from .locators import TensorMainPageLocators

class TensorMainPage(BasePage):
    def should_be_block_power_in_peoples(self):
        #power_in_peoples_block = WebDriverWait(self.browser, 25).until(EC.visibility_of_element_located(TensorMainPageLocators.POWER_IN_PEOPLE_BLOCK))
        power_in_peoples_block = self.browser.find_element(*TensorMainPageLocators.POWER_IN_PEOPLE_BLOCK)
        assert power_in_peoples_block, 'Block power in peoples should be present'

    def click_to_more_details(self):
        more_details = self.browser.find_element(*TensorMainPageLocators.MORE_DETAILS_IN_POWER_BLOCK)
        more_details.click()





    
