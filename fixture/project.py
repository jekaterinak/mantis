from model.project import Project


class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def open_projects_page(self):
        if not (self.app.wd.current_url.endswith("/manage_proj_page.php") and len(
                self.app.wd.find_elements_by_xpath("/html/body/table[3]/tbody/tr[1]/td/form/input[2]")) > 0):
            self.app.wd.find_element_by_link_text("Manage").click()
            self.app.wd.find_element_by_link_text("Manage Projects").click()

    project_cache = None

    def get_projects_list(self):
        if self.project_cache is None:
            self.open_projects_page()
            self.project_cache = []
            table_rows = self.app.wd.find_elements_by_css_selector(".width100 tr[class*='row-']")
            del table_rows[0]
            for element in table_rows:
                project_name = element.find_element_by_css_selector("td:nth-child(1) > a").text
                status = element.find_element_by_css_selector("td:nth-child(2)").text
                enabled = element.find_element_by_css_selector("td:nth-child(3)").text == "X"
                view_status = element.find_element_by_css_selector("td:nth-child(4)").text
                description = element.find_element_by_css_selector("td:nth-child(5)").text
                self.project_cache.append(
                    Project(project_name=project_name, status=status, enabled=enabled, view_status=view_status,
                            description=description))
        return list(self.project_cache)

    def change_field_value(self, field_name, text):
        if text is not None:
            self.app.wd.find_element_by_name(field_name).click()
            self.app.wd.find_element_by_name(field_name).clear()
            self.app.wd.find_element_by_name(field_name).send_keys(text)

    def fill_project_data(self, project):
        self.change_field_value("name", project.project_name)
        self.change_field_value("description", project.description)

    def count(self):
        self.open_projects_page()
        return len(self.app.wd.find_elements_by_css_selector(".width100 a[href*='project_id']"))

    def add(self, project):
        self.open_projects_page()
        # init project creation
        self.app.wd.find_element_by_xpath("/html/body/table[3]/tbody/tr[1]/td/form/input[2]").click()
        # fill project form
        self.fill_project_data(project)
        # submit contact creation
        self.app.wd.find_element_by_css_selector("tr:nth-child(7) > td > input").click()
        self.project_cache = None

    def select_project_by_id(self, project_id):
        self.app.wd.find_element_by_css_selector(".width100 a[href*='project_id=%s']" % project_id).click()

    def delete_project_by_id(self, id):
        self.open_projects_page()
        self.select_project_by_id(id)
        self.app.wd.find_element_by_css_selector("div.border.center input.button").click()
        self.app.wd.find_element_by_css_selector("form input.button").click()
        self.project_cache = None
