# config.py
import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='actividad4'
)
