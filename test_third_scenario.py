import os
from .pages.sbis_main_page import SbisMainPage
from .pages.sbis_download_page import SbisDownloadPage
import time

def test_downloaded_file_test_size(browser):
    link = 'https://sbis.ru/'
    sbis_main_page = SbisMainPage(browser, link)
    sbis_main_page.open()
    sbis_main_page.click_to_downoload_local_version()
    sbis_download_page = SbisDownloadPage(browser, browser.current_url)
    sbis_download_page.click_to_plugin_for_windows()
    sbis_download_page.click_to_download_web_installer()
    # Check size file
    file_size = os.path.getsize(r'C:\Users\User\Desktop\My folder\My python scripts\github clone project\tns\test_case_tensor\downloads\sbisplugin-setup-web.exe')
    file_size_mb = round(file_size / 1048576, 2)
    print(file_size_mb)
    assert file_size_mb == 11.48, "Файл не равен 11.48"