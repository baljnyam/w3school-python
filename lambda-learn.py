x = lambda a, b, c : a + b + c
print(x(5, 9, 2))

x = lambda a, b : a * b
print(x(5, 8))

x = lambda a, b, c: a + b + c

print(x(5,6,7))

def myfunc(n):
       return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(1))

def myfunc(n):
       return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

#Create a lambda function that takes one parameter (a) and returns it.
x = labda a : a
