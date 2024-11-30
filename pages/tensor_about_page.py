from .base_page import BasePage
from .locators import TensorAboutPageLocators

class TensorAboutPage(BasePage):
    def link_should_be_about(self):
        real_link = self.browser.current_url
        about_link = 'https://tensor.ru/about'
        assert real_link == about_link, 'More details are not sent to about the company'

    def pictures_in_working_block_should_be_same(self):
        pictures_in_working_block = WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located(TensorAboutPageLocators.PICTURES_IN_BLOCK_WORKING))
        self.check_same_images_sizes(pictures_in_working_block)