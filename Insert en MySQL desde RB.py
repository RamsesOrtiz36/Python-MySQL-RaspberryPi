# Bibliotecas
import mysql.connector

# Conexión
cnx = mysql.connector.connect(user='RamsesRB', password='pi', host='192.168.1.67', database='CodigoIoT')

# Cursor
cursor = cnx.cursor()

query_insert = "INSERT INTO rfid (nombre,texto,rfid) VALUES ('Ramses Ortiz','Test Python 8',865485648652);"

# Ejecutar cursor
cursor.execute (query_insert)

# Asegurarse de realizar la operacion en BD
cnx.commit()
print ("Query Ok")

# Cerrar
cursor.close()
cnx.close()