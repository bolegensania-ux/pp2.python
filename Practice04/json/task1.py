# there is a biult-in module in python for json

# import json

# To convert from python to json --> we use json.dumps() method

"""
example:

import json

x = {"name" : "John", "age" : 30, "city" : "New York"}

y = json.dumps(x)

print(y)
"""

# To convert from json to python --> we use json.loads() method

"""
example:

import json

x = '{"name" : "John", "age" : 30, "city" : "New York"}'

y = json.loads(x)

print(y["age"])
"""

# JSON - is a Java Script Notation, that helps to store and exchange data over the internet, or save in files

import json
with open("sample-data json") as file:
    data = json.load(file)

print("Interface status")
print("=" * 80)
print(f"{'DN':50} {'Speed':10} {'MTU':5}")

for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    speed = attributes["speed"]
    mtu = attributes["mtu"]

    print(f"{dn:50} {speed:10} {mtu:5}")