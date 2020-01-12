try:
       print(x)
except:
       print("An exception occured")

try:
       print(x)
except NameError:
       print("Variable x is not defined")
except:
       print("Someting else went wrong")

try:
       print("Hello")

except:
       print("Something went wrong")
else:
       print("Nothing went wrong")

try:
       print(x)
except:
       print("Something went wrong")
finally:
       print("The 'try except' is finished")

try:
       f = open("demofile.txt")
       f.write("Lorum Ipsum")
except:
       print("Something went wrong when writing to the life")
finally:
       f.close()
