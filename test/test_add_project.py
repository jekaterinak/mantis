import string
import random
import pytest
from model.project import Project


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Project(project_name=random_string("project_name", 15), description=random_string("description", 20), )
    for i in range(5)
]


@pytest.mark.parametrize("project", testdata)
def test_add_project(app, project):
    old_projects = app.project.get_projects_list()
    app.project.add(project)
    new_projects = app.project.get_projects_list()
    assert len(old_projects) + 1 == len(new_projects)
    project.project_name = app.remove_spaces( project.project_name)
    project.description = app.remove_spaces(project.description)
    old_projects.append(project)
    assert sorted(old_projects, key=Project.pr_name) == sorted(new_projects, key=Project.pr_name)
