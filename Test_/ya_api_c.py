import requests

TOKEN = "token" # введите свой токен


url = 'https://cloud-api.yandex.net:443/v1/disk/resources'


def dev_folder(path: str):
    params = {'path': path}
    headers = {'Content-Type': 'application/json',
               'Authorization': TOKEN}
    response = requests.api.put(url, headers=headers, params=params)
    return response.status_code

def del_folder(path: str):
    params = {'path': path}
    headers = {'Content-Type': 'application/json',
               'Authorization': TOKEN}
    response = requests.api.delete(url, headers=headers, params=params)
    return response.status_code