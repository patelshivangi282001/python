import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  port = 3308,
  user="root",
  password="",
  database="newdata"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)