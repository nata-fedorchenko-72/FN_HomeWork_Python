from ProjectAPI import ProjectApi

url = ProjectApi("https://ru.yougile.com/api-v2")


def test_create_progect_positive():
    my_list = url.get_list_project()
    num_project = my_list['paging']['count']
    list_orig = (num_project)

    name = "Креатив"
    user = {"bebdab3a-b10e-42c5-b146-ce022fcd5d1d": "admin"}
    result = url.creat_project(name, user)
    new_id = result["id"]

    my_list = url.get_list_project()
    num_project = my_list['paging']['count']
    list_new = (num_project)

    new_company = url.get_project(new_id)

    assert list_new - list_orig == 1
    assert my_list[-1]["name"] == name
    assert my_list['title'][-1]["id"] == new_id

def test_modified_project():
    name = "Креатив"
    user = {"bebdab3a-b10e-42c5-b146-ce022fcd5d1d": "admin"}
    result = url.creat_project(name, user)
    new_id = result["id"]

    new_name = "Креативный проект"
    modif_project = url.modified_project(new_name, new_id)

    assert modif_project[-1]["name"] == new_name
    

