from ProjectAPI import ProjectApi

url = ProjectApi("https://ru.yougile.com/api-v2")
key = "tnE4FaqWGuFipQbwwiWHEenkHkzbQdSDfVJczvOdiJDihDzs1DUjeSzsoniyRnHy"


def test_create_progect_positive():
    title = "Креатив"
    user = {"bebdab3a-b10e-42c5-b146-ce022fcd5d1d": "admin"}
    result = url.creat_project(title, user, key)
    assert result.status_code == 201


def test_get_projects_positive():
    result = url.get_list_project(key)
    assert result.status_code == 200
    assert result.json()['content'][-1]['title'] == 'Креатив'


def test_get_projects_negative():
    result = url.get_list_project(key=None)
    assert result.status_code == 401


def test_create_project_negative():
    title = ""
    user = {"bebdab3a-b10e-42c5-b146-ce022fcd5d1d": "admin"}
    result = url.creat_project(title, user, key)
    assert result.status_code == 400


def test_modified_project_positive():
    name = "Креатив"
    user = {"bebdab3a-b10e-42c5-b146-ce022fcd5d1d": "admin"}
    result = url.creat_project(name, user, key)
    new_id = result.json()["id"]

    new_name = "Креативный проект"
    url.modified_project(new_name, new_id, key)
    assert result.status_code == 201


def test_modified_project_negative():
    name = "Креатив"
    user = {"bebdab3a-b10e-42c5-b146-ce022fcd5d1d": "admin"}
    result = url.creat_project(name, user, key)
    result.json()["id"]

    new_name = "Креативный проект"
    modif_project = url.modified_project(new_name, "", key)
    assert modif_project.status_code == 404
