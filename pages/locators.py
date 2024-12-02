from selenium.webdriver.common.by import By

class SbisMainPageLocators():
    CONTACT_LINK = (By.CSS_SELECTOR, '.sbisru-Header__menu-item-1')
    MORE_OFFICES_LINK = (By.CSS_SELECTOR, '.sbisru-Header-ContactsMenu__items-visible .sbisru-link')
    DOWNLOAD_LOCAL_VERSION_LINK = (By.XPATH, '//a[contains(text(), "Скачать локальные версии")]')

class SbisContactPageLocators():
    TENSOR_LOGO = (By.CSS_SELECTOR, '#contacts_clients .sbisru-Contacts__logo-tensor.mb-12')
    SPECIFIC_REGION = (By.CSS_SELECTOR, '.sbisru-Contacts__relative .sbis_ru-Region-Chooser__text')
    SPECIFIC_PARTNERS = (By.CSS_SELECTOR, '.sbisru-Contacts-List__name')
    REGION_KAMCHATSKY_KRAY = (By.XPATH, '//span[contains(text(), "41 Камчатский край")]')

class SbisDownloadPageLocators():
    WINDOWS_TAB_IN_PLUGIN = (By.XPATH, "//span[text()='Windows']")
    DOWNLOAD_WEB_INSTALLER = (By.CSS_SELECTOR, '[href="https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe"]')

class TensorMainPageLocators():
    POWER_IN_PEOPLE_BLOCK = (By.CSS_SELECTOR, '.tensor_ru-Index__block4-content.tensor_ru-Index__card')
    MORE_DETAILS_IN_POWER_BLOCK = (By.CSS_SELECTOR, '.tensor_ru-Index__block4-content .tensor_ru-link')

class TensorAboutPageLocators():
    PICTURES_IN_BLOCK_WORKING = (By.CSS_SELECTOR, '.tensor_ru-About__block3-image')

