import requests
import json
import var


def create_iteration(url, parent, child, start_date=None, finish_date=None):
    url = f"{url}/{parent}?{var.azure_request['params']}"
    body = {"name": child,"attributes": {"startDate": start_date,"finishDate": finish_date}}
    print (url)
    print (str(body))
    req = requests.post(url, headers=var.azure_request['headers'], data=json.dumps(body), auth=(var.username, var.token))
    print(req.status_code)
    print(req.headers)
    print(req.text)



for root_parent in var.root_parents:
    create_iteration(url=var.azure_request['base_url'], parent=root_parent, child=var.year)
    for j,sprint_date in enumerate(var.dates):
        sub_url = f"{var.azure_request['base_url']}/{root_parent}"
        create_iteration(
            url=sub_url,
            parent=var.year,
            child=f"{var.year}{' - '}{j:02d}",
            start_date=var.dates["Start_Date"],
            finish_date=var.dates["Finish_Date"]
        )