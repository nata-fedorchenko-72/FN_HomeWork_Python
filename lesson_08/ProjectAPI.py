import requests


class ProjectApi:

    def __init__(self, url):
        self.url = url

    def get_list_project(self, key):
        my_headers = {
            'Authorization': f'Bearer {key}'
            }
        resp = requests.get(self.url + "/projects", headers=my_headers)
        return resp

    def get_project(self, id, key):
        my_headers = {
            'Authorization': f'Bearer {key}'
            }
        resp = requests.get(
            self.url + "/projects/" + str(id), headers=my_headers
            )
        return resp

    def create_project(self, name, user, key):
        project = {
            "title": name,
            "users": user
            }
        my_headers = {
            'Authorization': f'Bearer {key}'
            }
        resp = requests.post(
            self.url + "/projects", json=project, headers=my_headers
            )
        return resp

    def modified_project(self, new_name, new_id, key):
        project = {
            "title": new_name
            }
        my_headers = {
            'Authorization': f'Bearer {key}'
            }
        resp = requests.put(
            self.url + "/projects/" + str(new_id),
            json=project, headers=my_headers
            )
        return resp

    def delete_project(self, project_id, key):
        project = {
            "deleted": True
            }
        my_headers = {
            'Authorization': f'Bearer {key}'
            }
        resp = requests.put(
            self.url + f"/projects/{project_id}",
            json=project, headers=my_headers
            )
        return resp
