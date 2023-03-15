import json
import sys

user_list = []
with open("approver.json", "r") as file:
    data = json.load(file)


for user in data["users"]:
    user_list.append(user["user_id"].strip())


if sys.argv[1] in user_list:
    print("preesent")
else:
    sys.exit(1)
