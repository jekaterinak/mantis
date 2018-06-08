from selenium import webdriver
from fixture.session import SessionHelper
from fixture.project import ProjectHelper
from fixture.james import JamesHelper
from fixture.signup import SignupHelper
from fixture.mail import MailHelper
from fixture.soap import SoapHelper
import re


class Application:

    def __init__(self, browser, config):
        if browser == "firefox":
            self.wd = webdriver.Firefox(capabilities={"marionette": False})
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.session = SessionHelper(self)
        self.project = ProjectHelper(self)
        self.james = JamesHelper(self)
        self.signup = SignupHelper(self)
        self.mail = MailHelper(self)
        self.soap = SoapHelper(self, config["soap"])
        self.config = config
        self.base_url = config['web']['base_URL']


    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        if not (self.wd.current_url.endswith("/addressbook/") and len(
                self.wd.find_elements_by_id("search-az")) > 0):
            self.wd.get(self.base_url)

    def clear_phones(self, s):
        return re.sub("[() -]", "", s)

    def remove_spaces(self, t):
        trimmed = t.strip()
        return re.sub("[ ]+", " ", trimmed)

    def destroy(self):
        self.wd.quit()
