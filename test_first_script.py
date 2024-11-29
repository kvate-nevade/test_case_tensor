from .pages.sbis_main_page import SbisMainPage
from .pages.sbis_contact_page import SbisContactPage
from .pages.tensor_main_page import TensorMainPage

from time import sleep

def test_check_block_power_in_peoples(browser):
    link = 'https://sbis.ru/'
    page = SbisMainPage(browser, link)
    page.open()
    page.click_to_contacts()
    page.click_to_more_offices()
    contact_page = SbisContactPage(browser, browser.current_url)
    contact_page.click_to_tensor_logo()
    sleep(3)
    tensor_page = TensorMainPage(browser, browser.current_url)
    print(browser.current_url)
    sleep(15)
    tensor_page.should_be_block_power_in_peoples() # НИХУЯ НЕ РАБОТАЕТ ПОТОМУ ЧТО МЫ НЕ ФОКУСИМ ВТОРУЮ СТРАНИЧКУ

    



