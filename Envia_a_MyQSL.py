#Biblotecas
import mysql.connector

#conexión
cnx=mysql.connector.connect(user='Ramses',password='Tanis36',host='127.0.0.1',database='CodigoIoT')

#funcion cursor
cursor=cnx.cursor()

#Peticón para insertar valores a MySQL 
query_insert="INSERT INTO rfid (nombre,texto,rfid) VALUES ('Ramses Ortiz','Test Python 4',898765);"

#Ejecutar funcion cursro con query_insert de parametro
cursor.execute(query_insert)

#Mensaje para segurarse que se relalizo la inserción de datos a tabla en MySQL
cnx.commit()
print ("Query Ok")

#cerrar 
cursor.close()
cnx.close()
