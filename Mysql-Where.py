import mysql.connector

mydb = mysql.connector.connect(
       host = "127.0.0.1",
       user = "root",
       passwd = "",
       database = "mydatabase"
       )

mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address = 'Park Lane 38' "

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
       print(x)
