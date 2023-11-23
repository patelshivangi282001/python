import mysql.connector

mydb = mysql.connector.connect(
  host = "127.0.0.1",
  port = "3308",
  user = "root",
  password = "",
  database = "newdata"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255), address VARCHAR(255))")
