from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    country_list = (By.XPATH, '//body/div[1]/div[1]/div[1]/a')

class OpenedCountryResultsPageLocators(object):
    """A class for search results locators. All search results locators should come here"""
    pass