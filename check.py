import mysql.connector

cnx = mysql.connector.connect(user='root', password='rootPass',
                              host='localhost',
                              database='bdms')

print('so far so good')