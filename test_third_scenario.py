import os
from .pages.sbis_main_page import SbisMainPage
from .pages.sbis_download_page import SbisDownloadPage
import time

def test_downloaded_file_test_size(browser, download_dir):
    link = 'https://sbis.ru/'
    sbis_main_page = SbisMainPage(browser, link)
    sbis_main_page.open()
    sbis_main_page.click_to_downoload_local_version()
    sbis_download_page = SbisDownloadPage(browser, browser.current_url, download_dir)
    sbis_download_page.click_to_plugin_for_windows()
    sbis_download_page.click_to_download_web_installer()
    sbis_download_page.wait_for_file('sbisplugin-setup-web.exe')
    sbis_download_page.check_size_download_file('sbisplugin-setup-web.exe')