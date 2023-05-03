import mysql.connector
from mysql.connector.plugins import caching_sha2_password


# connect to the database server
try:
    conn=mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='password',
        database='indigo'

    )
    mycursor = conn.cursor()
    print('connection established')
except:
    print('connection error')

# create a database on the database server
##mycursor.execute("CREATE DATABASE indigo")
##conn.commit()
# create a table
# airport-> airport-id | code | name|city
##mycursor.execute(
    #"""
   # CREATE TABLE airport(
    #airport_id INTEGER PRIMARY KEY,
    #code VARCHAR(10) NOT NULL,
    #city VARCHAR(50) NOT NULL,
    #name VARCHAR(255) NOT NULL
    #)
    #"""
#)
#conn.commit()

# INSERT data to the table
#mycursor.execute("""
#INSERT INTO airport VALUES
#(1,'DEL', 'New Delhi','IGIA'),
#(2,'CCU','Kolkata','NSCA'),
#(3,'BOM','Mumbai','CSMA'
#)
#""")
#conn.commit()

# SEARCH/Retrieve
#mycursor.execute("SELECT * FROM airport WHERE airport_id>1")
#data=mycursor.fetchall()
# print(data)

# UPDATE
#mycursor.execute("""
#UPDATE airport
#SET name='Bombay'
#WHERE airport_id=3
#""")
#conn.commit()
# Retriving after update
#mycursor.execute("SELECT * FROM airport WHERE airport_id>1")
#data=mycursor.fetchall()
#print(data)


# DELETE
mycursor.execute("DELETE FROM airport WHERE airport_id=3")
conn.commit()
# Retriving after delete
mycursor.execute("SELECT * FROM airport")
data=mycursor.fetchall()
print(data)
