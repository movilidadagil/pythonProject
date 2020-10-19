from selenium import webdriver
import os
import json
from urllib.parse import urljoin

from pages.mainpage.mainpagelocators import MainPageLocators


class Base:
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Base()
        return cls.instance


    def __init__(self):
        global  settings
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'settings.json')) as f:
            settings = json.load(f)
        if str(settings['browser']).lower() == "firefox":
            self.driver = webdriver.Firefox()
        elif str(settings['browser']).lower() == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--start-fullscreen")
            self.driver = webdriver.Chrome(chrome_options=options)
        else:
            self.driver = webdriver.Firefox()

    def get_driver(self):
        return self.driver

    def load_website(self):
        self.driver.get(settings['url'])

    def goto_page(self, page):
        self.driver.get(urljoin(settings['url'], page.lower()))

    def verify_component_exists(self, component, order):
               print(self.driver.find_elements_by_xpath('//body/div[1]/div[1]/div[1]/a/div[2]')[int(order)].text)
               component = component.split(' ')[1].replace('"', "")
               assert component in self.driver.find_elements_by_xpath('//body/div[1]/div[1]/div[1]/a/div[2]')[int(order)].text, \
                "Component {} not found on page".format(component)



    def close_browser(self):
        self.driver.quit()

base = Base.get_instance()
