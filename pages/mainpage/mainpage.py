from pages.mainpage.mainpagelocators import MainPageLocators
from base.base import  base


class MainPage():
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = MainPage()
        return cls.instance

    def __init__(self):
        self.driver = base.get_driver()


    def is_title_matches(self):
        """Verifies that the hardcoded text "Python" appears in page title"""
        return "Property Finder Group" in self.driver.title

    def click_country_thumb(self, country):
        """Triggers the search"""
        countries  = self.driver.find_element(*MainPageLocators.country_list)
        for item in countries:
            if country == item.text:
                item.click()


mainpage = MainPage.get_instance()
