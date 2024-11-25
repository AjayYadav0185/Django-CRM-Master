import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost', 
    user = 'root', 
    password = ''
)

cursorObj = dataBase.cursor()

cursorObj.execute("CREATE DATABASE sampleKing")

print('sampleKing created successfully')
# dataBase.close()
