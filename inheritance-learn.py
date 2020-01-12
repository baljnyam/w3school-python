class Person:
       def __init__(self, fname, lname):
              self.firstname = fname
              self.lastname = lname

       def printname(self):
              print(self.firstname, self.lastname)

       # Using the Person class to creat an object, and then execute the printname method:

x = Person("John", "Poe")
x.printname()

class Student(Person):
       pass
y = Student("Moke", "Wallece")
y.printname()

class Student2(Person):
       def __init__(self, fname, lname, year):
              Person.__init__(self, fname, lname)
              self.graduationyear = year

x = Student2("Mike", "Dorcy", 13)

class Student3(Person):
       def __init__(self, fname, lname, year):
              Person.__init__(self, fname, lname)
              self.graduationyear = year

       def welcome(self):
              print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
x = Student3("Dorj", "Daddy", 2018)
print(x.welcome())
