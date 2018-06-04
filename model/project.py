class Project:
    def __init__(self, project_name=None, status="development", enabled=True, inherit_global=True, view_status="public",
                 description=None):
        self.project_name = project_name
        self.status = status
        self.enabled = enabled
        self.inherit_global = inherit_global
        self.view_status = view_status
        self.description = description

    def __repr__(self):
        return '%s:%s' % (self.project_name, self.description)

    def __eq__(self, other):
        res = (self.project_name == other.project_name and self.status == other.status \
               and self.enabled == other.enabled and self.view_status == other.view_status and \
               self.description == other.description)
        return res

    def pr_name(self):
        return self.project_name
