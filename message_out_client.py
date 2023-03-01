import requests


out_data = {"user": "ed214", "message": ":)"}
r = requests.post("http://vcm-21170.vm.duke.edu:5001/add_message", json=out_data)
print(r.status_code)
print(r.text)