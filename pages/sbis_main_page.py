from .base_page import BasePage
from .locators import SbisMainPageLocators

class SbisMainPage(BasePage):
    def click_to_contacts(self):
        contact_link = self.browser.find_element(*SbisMainPageLocators.CONTACT_LINK)
        contact_link.click()

    def click_to_more_offices(self):
        more_offices = self.browser.find_element(*SbisMainPageLocators.MORE_OFFICES_LINK)
        more_offices.click()
        

    
