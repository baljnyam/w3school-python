# A Regex, or Regular Expression,is a sequence of characters that forms a search pattern regEx can be used to check if string contains the specified search pattern
# Python has a built-in package called re, which can be used to work with Regular Expression.

import  re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

print(x == txt)


str = "The rain in Sapain"
x = re.findall("ai", str)
print(x)

str = "The rain in Spain"

#Find all lower case chaacters alphabetically between "a" and "m":

x = re.findall("[a-m]", str)
print(x)

str = "That will be 59 dollars"

#Find all digit characters:

x = re.findall("\d", str)
print(x)

str = "hello world"

# Search for a sequence that starts with "he", followed by two (any) characters, and an "o":

x = re.findall("he..o", str)
print(x)

x = re.findall("^hello", str)
if(x):
       print("Yes, the string starts with 'hello'")
else:
       print("No match")

str = "The rain in Spain falls mainly in the plain!"

# Check if the string contains "ai" followed by 0 or more "x" characters:

x = re.findall("aix*", str)

print(x)

if(x):
       print("Yes, there is at least one match!")
else:
       print("No match")

str = "The rain in Spain falls mainly in the plain!"

#Check if the string contains "ai" followed by 1 or more "x" characters:

x = re.findall("aix+", str)

print(x)

if(x):
       print("Yes, there is at least one match!")
else:
       print("No match!")

x = re.findall("al{2}", str)

print(x)

if(x):
               print("Yes, there is at least on match!")
else:
               print("No match")
x = re.findall("falls|stays", str)

print(x)

if(x):
       print("Yes, there is at least on match!")
else:
       print("No match")

str = "The rain in Spain"

x = re.findall("[arn]", str)

print(x)

if(x):
       print("Yes, there is at least one match!")
else:
       print("No match")

# Check if the string has any characters between a and n:

x = re.findall("[a-n]", str)
print(x)

if(x):
       print("Yes, there is at least one match!")
else:
       print("No match")

x = re.findall("[^arn]", str)

print(x)

if(x):
       print("Yes, there is at least one match!")
else:
       print("No match")

x = re.findall("[0123]", str)

print(x)

if(x):
       print("Yes, there is at least one match !")
else:
       print("No match")

str = "8 times before 11:45 AM"

# check if the string has any digits:

x = re.findall("[0-9]", str)

print(x)

if(x):
       print("Yes, there is at least one match!")
else:
       print("no match!")

str = "The rain in Spain"
x = re.findall("Portugal", str)
print(x)

x  = re.search("\S", str)
print("The first white-space chatacter is located in position:", x.start())

x = re.split("\s", str)
print(x)

x = re.split("\s", str, 1)
print(x)

x = re.sub("\s", "9", str)
print(x)

x = re.sub("\s","9", str, 2)
print(x)

x = re.search("ai", str)
print(x)

x = re.search(r"\bS\w+", str)
print(x.span())

x = re.search(r"\bS\w+", str)
print(x.string)

x = re.search(r"\bS\w+", str)
print(x.group())



