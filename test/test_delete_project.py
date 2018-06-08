from random import randrange, choice
from model.project import Project


def test_delete_project(app):
    if app.project.count() == 0:
        app.project.add(Project(project_name="testname", description="testdescription"))
    old_projects = app.soap.get_projects()
    project_to_delete = choice(old_projects)
    app.project.delete_project_by_id(project_to_delete.id)
    old_projects.remove(project_to_delete)
    assert len(old_projects) == app.project.count()
    new_projects = app.soap.get_projects()
    assert sorted(old_projects, key=Project.pr_name) == sorted(new_projects, key=Project.pr_name)



