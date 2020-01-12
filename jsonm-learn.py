import json

# some JSON:

x = '{"name": "John", "age": 30, "city": "New York"}'

# parse x:

y = json.loads(x)

# the result is a Python dictionary

print(y["age"])

import json

# a python object (dict):
x = {
       "name": "John",
       "age": 30,
       "city": "New York"
       }

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

# it is possible to convert following objects: dict list tuple string int float True False NONE

import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "banana"]))
print(json.dumps(("apple", "banana")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))


import json

x = {
       "name": "John",
       "age": 30,
       "married": True,
       "divorced": False,
       "children": ("Ann","Billy"),
       "pets": None,
       "cars": [
              {"model": "BMW 230", "mpg": 27.5},
              {"model": "Ford Edge", "mpg": 24.1}
              ]
       }
print(json.dumps(x))

print(json.dumps(x, indent=4))

print(json.dumps(x, indent=4, separators=(". ", " = ")))

print(json.dumps(x, indent=4, sort_keys=True))
