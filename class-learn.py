class MyClass:
       x = 5
p1 = MyClass()
print(p1.x)

class Person:
       def __init__(self, name, age):
              self.name = name
              self.age = age

p2 = Person("John", 36)

print(p2.name)
print(p2.age)

class Person2:
       def __init__(self, name, age):
              self.name = name
              self.age = age

       def myfunc(self):
              print("Hello my name is " + self.name)
       def myfunc2(self):
              print("Age is",self.age)
p3 = Person2("Enkhbat", 29)
p3.myfunc()
p3.myfunc2()

class Person3:
       def __init__(mysillyobject, name, age):
              mysillyobject.name = name
              mysillyobject.age = age

       def myfunc(abc):
              print("Hello my name is " + abc.name)
       def myfunc2(ddd):
              print("Age is", ddd.age)
p4 = Person3("Zaya", 28)
#del p4
p4.myfunc()
p4.myfunc2()

