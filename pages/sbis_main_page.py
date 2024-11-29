from .base_page import BasePage
from .locators import SbisMainPageLocators

class SbisMainPage(BasePage):
    def click_to_contact(self):
        contact_link = self.browser.find_element(*SbisMainPageLocators.CONTACT_LINK)
        contact_link.click()

    
