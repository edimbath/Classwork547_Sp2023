import requests


# r = requests.get("http://vcm-7631.vm.duke.edu:5002/get_patients/ed214")
# print(r)
# print(type(r))
# print(r.status_code)
# print(r.text)
# # branches = r.json()
# # print(branches)
# # for branch in branches:
# #     print(branch["message"])
# donor = F2 recipient = M4

# r = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/M4")
#print(r)
#print(type(s))
#print(s.status_code)
# print(r.text)
# branches = r.json()
# print(branches)
# for branch in branches:
#     print(branch["message"])
# F2 blood type is A-
# M4 blood type is A-

out_data = {"Name": "ed214", "Match": "Yes"}
r = requests.post("http://vcm-7631.vm.duke.edu:5002/match_check", json=out_data)
print(r.status_code)
print(r.text)
