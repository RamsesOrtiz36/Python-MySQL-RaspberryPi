#Biblioteca usada
import mysql.connector

#inicializar conexión a base de datos de MySQL
cnx = mysql.connector.connect(user='RamsesRB', password='pi', host='192.168.1.66', database='CodigoIoT')
cursor=cnx.cursor()         #Función Cursor

#Petición de datos a MySQL desde la tabla rfid
query =("SELECT id, nombre,rfid FROM rfid WHERE id = 9;")

#Ejecutar funsion cursor con la petición de datos a MySQL
cursor.execute(query)

res=cursor.fetchall ()

for x in res:
    print (x)
#cerrar funcion cursor
#cursor.close()
# Cerrar conexión a MySQL
#cnx.close()
#print("Fin de conexión a MySQL")
