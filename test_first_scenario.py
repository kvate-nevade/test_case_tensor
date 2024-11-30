from .pages.sbis_main_page import SbisMainPage
from .pages.sbis_contact_page import SbisContactPage
from .pages.tensor_main_page import TensorMainPage
from .pages.tensor_about_page import TensorAboutPage

from time import sleep

def test_check_block_power_in_peoples(browser):
    link = 'https://sbis.ru/'
    sbis_page = SbisMainPage(browser, link)
    sbis_page.open()
    sbis_page.click_to_contacts()
    sbis_page.click_to_more_offices()
    contact_page = SbisContactPage(browser, browser.current_url)
    contact_page.click_to_tensor_logo()
    contact_page.switch_to_window(2)
    tensor_page = TensorMainPage(browser, browser.current_url)
    tensor_page.should_be_block_power_in_peoples()

def test_more_details_go_to_about(browser):
    link = 'https://tensor.ru/'
    tensor_page = TensorMainPage(browser, link)
    tensor_page.open()
    tensor_page.click_to_more_details()
    tensor_about_page = TensorAboutPage(browser, browser.current_url)
    tensor_about_page.link_should_be_about()

def test_pictures_should_be_same_in_about_page(browser):
    link = 'https://tensor.ru/about'
    tensor_about_page = TensorAboutPage(browser, link)
    tensor_about_page.open()
    tensor_about_page.pictures_in_working_block_should_be_same()




