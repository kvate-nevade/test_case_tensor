import os
import time
from .base_page import BasePage
from .locators import SbisDownloadPageLocators

class SbisDownloadPage(BasePage):
    def __init__(self, browser, download_dir):
        self.browser = browser
        self.download_dir = download_dir

    def click_to_plugin_for_windows(self):
        window_tab_in_plugin = self.browser.find_element(*SbisDownloadPageLocators.WINDOWS_TAB_IN_PLUGIN)
        window_tab_in_plugin.click()
    
    def click_to_download_web_installer(self):
        web_installer = self.browser.find_element(*SbisDownloadPageLocators.DOWNLOAD_WEB_INSTALLER)
        web_installer.click()
"""
    def wait_for_file(self, filename, timeout=30):
        file_path = os.path.join(self.download_dir, filename)
        start_time = time.time()
        while not os.path.exists(file_path):
            if time.time() - start_time > timeout:
                raise TimeoutError(f"File {filename} didn't download in {timeout} seconds")
            time.sleep(1)
        return file_path

"""