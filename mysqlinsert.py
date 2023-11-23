import mysql.connector

mydb = mysql.connector.connect(
  host = "127.0.0.1",
  port = 3308,
  user = "root",
  password = "",
  database = "newdata"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('name1', 'address1'),
  ('name2', 'address2'),
  ('name3', 'address3'),
  ('name4', 'address4'),
  ('name5', 'address5'),
  ('name6', 'address6'),
  ('name7', 'address7'),
  ('name8', 'address8'),
  ('name9', 'address9'),
  ('name10', 'address10')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record was inserted.")