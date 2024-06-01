# Importing module 
import mysql.connector

# Creating connection object
mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "Himapaka_90"
)

# Printing the connection object 
cursor = mydb.cursor()