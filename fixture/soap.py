from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:
    def __init__(self, app, config):
        self.app = app
        self.config = config

    def can_login(self):
        client = Client(self.config["wsdl_URL"])
        try:
            client.service.mc_login(self.config["username"],
                                    self.config["password"])
            return True
        except WebFault:
            return False

    def get_projects(self):
        client = Client(self.config["wsdl_URL"])
        try:
            test = client.service.mc_projects_get_user_accessible(self.config["username"],
                                                                  self.config["password"])
            projects = [Project(project_name=i.name, description=i.description, id=i.id) for i in test]
            return projects
        except WebFault:
            return False
