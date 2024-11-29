from .pages.sbis_main_page import SbisMainPage

def test_user_should_click_to_contact():
    link = 'https://sbis.ru/'
    page = SbisMainPage(browser, link)
    page.open()
    page.click_to_contact()


