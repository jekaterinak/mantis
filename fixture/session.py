class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        self.app.open_home_page()
        self.app.wd.find_element_by_name("username").click()
        self.app.wd.find_element_by_name("username").clear()
        self.app.wd.find_element_by_name("username").send_keys(username)
        self.app.wd.find_element_by_name("password").click()
        self.app.wd.find_element_by_name("password").clear()
        self.app.wd.find_element_by_name("password").send_keys(password)
        self.app.wd.find_element_by_css_selector('input[type="submit"]').click()

    def logout(self):
        self.app.wd.find_element_by_link_text("Logout").click()

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        return len(self.app.wd.find_elements_by_link_text("Logout")) > 0

    def is_logged_in_as(self, username):
        return self.get_logged_user() == username

    def get_logged_user(self):
        return self.app.wd.find_element_by_css_selector("td.login-info-left span").text

    def ensure_login(self, username, password):
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)
