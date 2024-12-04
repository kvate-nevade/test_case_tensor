import os
import time
from .base_page import BasePage
from .locators import SbisDownloadPageLocators

class SbisDownloadPage(BasePage):
    def __init__(self, browser, url, download_dir):
        self.browser = browser
        self.url = url
        self.download_dir = download_dir

    def click_to_plugin_for_windows(self):
        window_tab_in_plugin = self.browser.find_element(*SbisDownloadPageLocators.WINDOWS_TAB_IN_PLUGIN)
        window_tab_in_plugin.click()
    
    def click_to_download_web_installer(self):
        web_installer = self.browser.find_element(*SbisDownloadPageLocators.DOWNLOAD_WEB_INSTALLER)
        web_installer.click()

    def wait_for_file(self, filename, timeout=30):
        file_path = os.path.join(self.download_dir, filename)
        start_time = time.time()
        while not os.path.exists(file_path):
            if time.time() - start_time > timeout:
                raise TimeoutError(f"File {filename} didn't download in {timeout} seconds")
            time.sleep(1)
        return file_path

    def check_size_download_file(self, filename):
        text_file_size = float(self.browser.find_element(*SbisDownloadPageLocators.DOWNLOAD_WEB_INSTALLER).text.split(' ')[2])
        file_size = os.path.getsize(os.path.join(self.download_dir, filename))
        file_size_in_megabyte = round(file_size / 1048576, 2)
        assert file_size_in_megabyte == text_file_size, "File size webinstaller on https://sbis.ru/download?tab=plugin&innerTab=default is not equal to the real one"