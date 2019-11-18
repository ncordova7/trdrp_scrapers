#Connects to MySql Database.
import mysql.connector

print("Start")
cnx = mysql.connector.connect(user='karlhickel', password='jh33st789',host='35.197.114.82', database='geoData')
print("connected")
cnx.close()
