import requests


out_data = {"name": "Elizabeth Dimbath", "net_id": "ed214",
            "e-mail": "ed214@duke.edu"}
r = requests.post("http://vcm-21170.vm.duke.edu:5000/student", json=out_data)
print(r.status_code)
print(r.text)