from random import randrange
from model.project import Project


def test_delete_project(app):
    if app.project.count() == 0:
        app.project.add(Project(project_name="testname", description="testdescription"))
    old_projects = app.project.get_projects_list()
    index = randrange(len(old_projects))
    app.project.delete_project_by_index(index)
    assert len(old_projects) - 1 == app.project.count()
    new_projects = app.project.get_projects_list()
    old_projects[index:index + 1] = []
    assert sorted(old_projects, key=Project.pr_name) == sorted(new_projects, key=Project.pr_name)
