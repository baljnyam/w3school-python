import  mysql.connector

mydb = mysql.connector.connect(
       host = "localhost",
       user = "root",
       passwd = "",
       database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE Customers (CustomerID VARCHAR(255), customerName VARCHAR(255),  )")
