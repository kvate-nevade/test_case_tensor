from selenium.webdriver.common.by import By

class SbisMainPageLocators():
    CONTACT_LINK = (By.CSS_SELECTOR, '.sbisru-Header__menu-item-1')
    MORE_OFFICES_LINK = (By.CSS_SELECTOR, '.sbisru-Header-ContactsMenu__items-visible .sbisru-link')

class SbisContactPageLocators():
    TENSOR_LOGO = (By.CSS_SELECTOR, '#contacts_clients .sbisru-Contacts__logo-tensor.mb-12')

class TensorMainPageLocators():
    POWER_IN_PEOPLE_BLOCK = (By.CSS_SELECTOR, '.tensor_ru-Index__block4-content.tensor_ru-Index__card')