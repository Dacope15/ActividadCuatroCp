# test_db_connection.py
import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='actividad4'
)

cursor = db.cursor()
cursor.execute("SELECT DATABASE()")
result = cursor.fetchone()
print(f"Conectado a la base de datos: {result[0]}")
