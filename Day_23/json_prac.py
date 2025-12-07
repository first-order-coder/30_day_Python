import json

with open("./Day_23/json_prac.json") as f:
    text = f.read()
    data = json.loads(text) #load the json data as usable dict in python 

empty_lst = []
for state in data["states"]:
    empty_lst.append({"State Name":state["name"], 
                  "State Shorten": state["abbreviation"]})

with open("./Day_23/json_prac_1.json", "w") as f:
    json.dump(empty_lst, f, indent=2)