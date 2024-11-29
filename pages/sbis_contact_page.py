from .base_page import BasePage
from .locators import SbisContactPageLocators

class SbisContactPage(BasePage):
    def click_to_tensor_logo(self):
        contact_link = self.browser.find_element(*SbisContactPageLocators.TENSOR_LOGO)
        contact_link.click()



    
