from ProjectAPI import ProjectApi

url = ProjectApi("")
key = ""


def test_create_project_positive():
    title = "Креатив"
    user = {"bebdab3a-b10e-42c5-b146-ce022fcd5d1d": "admin"}
    result = url.create_project(title, user, key)
    my_id = result.json()["id"]
    assert result.status_code == 201
    assert result.json()["id"] == my_id


def test_get_projects_positive():
    result = url.get_list_project(key)
    assert result.status_code == 200
    assert result.json()['content'][-1]['title'] == 'Креатив'

    project_id = result.json()["content"][-1]["id"]
    url.delete_project(project_id, key)
    assert result.status_code == 200


def test_get_projects_negative():
    result = url.get_list_project(key=None)
    assert result.status_code == 401


def test_create_project_negative():
    title = ""
    user = {"bebdab3a-b10e-42c5-b146-ce022fcd5d1d": "admin"}
    result = url.create_project(title, user, key)
    assert result.status_code == 400


def test_modified_project_positive():
    name = "Skypro"
    user = {"bebdab3a-b10e-42c5-b146-ce022fcd5d1d": "admin"}
    result = url.create_project(name, user, key)
    new_id = result.json()["id"]

    new_name = "SkyPro"
    modif_response = url.modified_project(new_name, new_id, key)
    assert modif_response.status_code == 200
    updated_project = url.get_project(new_id, key).json()
    assert updated_project["title"] == new_name

    project_id = result.json()["id"]
    url.delete_project(project_id, key)
    assert result.status_code == 201


def test_modified_project_negative():
    name = "Здоровье"
    user = {"bebdab3a-b10e-42c5-b146-ce022fcd5d1d": "admin"}
    result = url.create_project(name, user, key)
    result.json()["id"]

    new_name = "Здоровье нации"
    modif_project = url.modified_project(new_name, "", key)
    assert modif_project.status_code == 404

    project_id = result.json()["id"]
    url.delete_project(project_id, key)
    assert result.status_code == 201
