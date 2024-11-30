from .pages.sbis_main_page import SbisMainPage
from .pages.sbis_contact_page import SbisContactPage

def test_should_be_region_and_partners(browser):
    link = 'https://sbis.ru'
    sbis_main_page = SbisMainPage(browser, link)
    sbis_main_page.open()
    sbis_main_page.click_to_contacts()
    sbis_main_page.click_to_more_offices()
    contact_page = SbisContactPage(browser, browser.current_url)
    contact_page.should_be_region_and_partners()

def test_pick_region_should_change_title_and_url(browser):
    link = 'https://sbis.ru/contacts'
    sbis_contact_page = SbisContactPage(browser, link)
    sbis_contact_page.open()
    sbis_contact_page.check_changing_partners_and_region_link_in_kamchatsky_krai()
    sbis_contact_page.check_url_and_title_kamchatsky_krai()
