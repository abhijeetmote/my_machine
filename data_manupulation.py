"""go to your terminal and execute the following command :

python -m pip install mysql-connector-python
Once its done, if you dont have install mysql for windows or macbook
for windows https://dev.mysql.com/downloads/installer/
for macbook https://dev.mysql.com/downloads/mysql/ 
Make sure you remeber the username and password

Thats it you are good to go.
"""

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root", # this would be default user
    password="abhijeetmote" # for simiplycity I gave simple pasword, dont share your password with anyone 
)

mycursor = mydb.cursor()

try:
    mycursor.execute("CREATE DATABASE mydatabase")
except:
    print("Database already exist")
    
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x) 

# lets create a table 
mycursor.execute("use mydatabase")
try:
    mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
except:
    print("Table already exist")

# Lets display the table 
mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)

mycursor.execute("INSERT INTO customers (name, address) VALUES (%s, %s)", ("Abhijeet", "Valley Ranch") )
mycursor.execute("INSERT INTO customers (name, address) VALUES (%s, %s)", ("Solapurkar Kaka", "lewisville") )

mydb.commit()

print(mycursor.rowcount, "record inserted.")

# retrive the data 
mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
