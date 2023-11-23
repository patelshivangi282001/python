import mysql.connector


mydb = mysql.connector.connect(

    host = "127.0.0.1",
    port = "3308",
    user = "root",
    password = ""
)

print(mydb)
