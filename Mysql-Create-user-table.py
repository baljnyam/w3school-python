import mysql.connector

mydb = mysql.connector.connect(
       host = "localhost",
       user = "root",
       passwd = "",
       database = "mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE  products (id VARCHAR(255), name VARCHAR(255))")
