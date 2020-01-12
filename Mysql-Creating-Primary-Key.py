import mysql.connector

mydb = mysql.connector.connect(
       host = "localhost",
       user = "root",
       passwd = "",
       database = "mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customersreal(id INT AUTO_INCREMENT KEY, name VARCHAR(255), address VARCHAR(255))")
