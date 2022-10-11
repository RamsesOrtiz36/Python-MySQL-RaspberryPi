# Bibliotecas
import mysql.connector
from time import sleep
import sys
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO

reader = SimpleMFRC522()
try:
    while True:
        #Lee el TAG o Tarjeta y toma sus valores de texto e id
        print ("hold a tag near the reader")
        id, text = reader.read()

        # Conexión
        cnx = mysql.connector.connect(user='RamsesRB', password='pi', host='192.168.1.67', database='CodigoIoT')

        # Cursor
        cursor = cnx.cursor()

        query_insert = "INSERT INTO rfid (nombre,texto,rfid) VALUES ('Ramses Ortiz',' " + text + "',"+ str(id) +");"

        # Ejecutar cursor
        cursor.execute (query_insert)

        # Asegurarse de realizar la operacion en BD
        cnx.commit()
        print ("Query Ok")
        sleep(5)

        # Cerrar cursor y conexion a mysql
        cursor.close()
        cnx.close()

except KeyboardInterrupt:
    GPIO.cleanup()
    raise
