import requests

base_url = "https://ru.yougile.com/api-v2"

def test_create_project():
    accounе = {
        "login": "nata.fedorchenko.72@gmail.com",
        "password": "Nata><fedoR~1972"
        }
    resp = requests.post(base_url+"/auth/companies", json=accounе)
    my_company = resp.json()["content"][0]["id"]
    assert resp.status_code ==200
    
    response_key = {
        "login": "nata.fedorchenko.72@gmail.com",
        "password": "Nata><fedoR~1972",
        "companyId": my_company
        }
    resp = requests.post(base_url+"/auth/keys", json=response_key)
    my_key = resp.json()["key"]
    assert resp.status_code == 201

    my_headers = {
        'Authorization': f'Bearer {my_key}'
        }
    resp = requests.get(base_url+"/projects", headers=my_headers)
    answer = resp.json()
    assert resp.status_code == 200

    my_headers = {
        'Authorization': f'Bearer {my_key}'
        }
    project = {
        "title": "SkyPro",
        "users": {"bebdab3a-b10e-42c5-b146-ce022fcd5d1d": "admin"}
        }

    resp = requests.post(base_url + "/projects", json=project, headers=my_headers)
    #key_project = resp.json()["key"]
    assert resp.status_code == 200
