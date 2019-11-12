
#from mysql.connector import (connection)
import mysql.connector

#cnx = connection.MySQLConnection(user="geoscrapingfinal1", password="jh33st789",host="35.197.114.82",database="geoData")
#print("connected")
#cnx.close()

print("Start")
cnx = mysql.connector.connect(user='karlhickel', password='jh33st789',host='35.197.114.82', database='geoData')
print("connected")
cnx.close()

#PGHOST = "35.247.75.81"
#PGDATABASE = "geoData"
#PGUSER = "karlhickel"
#PGPASSWORD = "907iscool"


#conn_string = "host="+ PGHOST +" port="+ "5432" +" dbname="+ PGDATABASE +" user=" + PGUSER \
#+" password="+ PGPASSWORD

#conn = psycopg2.connect(host="35.247.75.8",database="geoData", user="karlhickel", password="907iscool")
#conn=psycopg2.connect(conn_string)
#print("Connected!")




#line 89
 #37-38
 #907iscool


#cursor = con.curson()
#print("Hellohello")

#sql = "CREATE TABLE sql_test_a (ID VARCHAR2(4000BYTE),FIRST_NAME VARCHAR2(200 BYTE),LAST_NAME  VARCHAR2(200 BYTE)); )"
