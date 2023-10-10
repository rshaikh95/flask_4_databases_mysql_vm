# Importing module 
import mysql.connector

# Creating connection object
mydb = mysql.connector.connect(
	host = 'DB_HOST',
	user = 'DB_USERNAME',
	password = 'DB_PASSWORD'
)

# Printing the connection object 
print(mydb)
