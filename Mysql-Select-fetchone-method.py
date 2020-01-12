import mysql.connector

mydb = mysql.connector.connect(
       host = "127.0.0.1",
       user = "root",
       passwd = "",
       database = "mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchone()


print(myresult)
