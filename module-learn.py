import mymodule

a = mymodule.person1["age"]

print(a)

import mymodule as mc

a = mc.person1["age"]
print(a)

import platform

x = platform.system()
print(x)

from mymodule import person1

print(person1["age"])
