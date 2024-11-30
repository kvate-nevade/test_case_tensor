from .base_page import BasePage
from .locators import SbisContactPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SbisContactPage(BasePage):
    def click_to_tensor_logo(self):
        contact_link = self.browser.find_element(*SbisContactPageLocators.TENSOR_LOGO)
        contact_link.click()

    def should_be_region_and_partners(self):
        self.should_be_specific_region()
        self.should_be_specific_partners()

    def should_be_specific_region(self):
        specific_region = self.browser.find_element(*SbisContactPageLocators.SPECIFIC_REGION)
        assert specific_region, 'Region is not show in contacts.'

    def should_be_specific_partners(self):
        specific_partners = self.browser.find_elements(*SbisContactPageLocators.SPECIFIC_PARTNERS)
        assert specific_partners, 'Partners is not show in contacts.'

    def check_changing_partners_and_region_link_in_kamchatsky_krai(self):
        start_partners_list = self.browser.find_elements(*SbisContactPageLocators.SPECIFIC_PARTNERS)
        region_lists = self.browser.find_element(*SbisContactPageLocators.SPECIFIC_REGION)
        region_lists.click()
        self.browser.find_element(*SbisContactPageLocators.REGION_KAMCHATSKY_KRAY).click()
        WebDriverWait(self.browser, 10).until(EC.title_contains("Камчатский край"))
        shoosed_region_text = self.browser.find_element(*SbisContactPageLocators.SPECIFIC_REGION).text
        finish_partners_list = self.browser.find_elements(*SbisContactPageLocators.SPECIFIC_PARTNERS)
        assert shoosed_region_text == 'Камчатский край', 'Region link must be Камчатский край'
        assert set(start_partners_list) != set(finish_partners_list), 'Partners list must be changing'

    def check_url_and_title_kamchatsky_krai(self):
        kamchatsky_krai_title = self.browser.title
        #return link without excess part https and other
        url_region_part = self.browser.current_url.split('?')[0].split('/')[-1]
        assert 'Камчатский край' in kamchatsky_krai_title, 'Title must contain Камчатский край'
        assert url_region_part == '41-kamchatskij-kraj', 'Url must contain 41-kamchatskij-kraj'

        



    
