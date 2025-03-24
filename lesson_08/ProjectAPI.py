import requests


class ProjectApi:

    def __init__(self, url):
        self.url = url

    def get_auth(self, login="nata.fedorchenko.72@gmail.com", password="Nata><fedoR~1972"):
        accounе = {
            "login": login,
            "password": password
            }
        resp = requests.post(self.url+"/auth/companies", json=accounе)
        return resp.json()["content"][0]["id"]
    
    def get_key(self, login="nata.fedorchenko.72@gmail.com", password="Nata><fedoR~1972"):
        response_key = {
            "login": login,
            "password": password,
            "companyId": "6ae1affa-8587-472d-b688-716660196adc"
            }
        resp = requests.post(self.url+"/auth/keys", json=response_key)
        return resp.json()["key"]
    
    def get_list_project(self):
        my_headers = {
            'Authorization': f'Bearer {self.get_key()}'
            }
        resp = requests.get(self.url+"/projects", headers=my_headers)
        return resp.json()
    
    def get_project(self, id):
        resp = requests.get(self.url+"/company/"+str(id))
        return resp.json()

    def creat_project(self, name, user):
        project = {
            "title": name,
            "users": user
            }
        my_headers = {
            'Authorization': f'Bearer {self.get_key()}'
            }
        resp = requests.post(
            self.url + "/projects", json=project, headers=my_headers)
        return resp.json()
    
    def modified_project(self, new_name, new_id):
        project = {
            "title": new_name
            }
        my_headers = {
            'Authorization': f'Bearer {self.get_key()}'
            }
        resp = requests.put(
            self.url+ "/projects/"+ str(new_id), json=project, headers=my_headers)
        return resp.json()
