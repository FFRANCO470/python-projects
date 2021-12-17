import mysql.connector

def conectar():
    database = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="adsi2067725"
    )
    cursor = database.cursor(buffered=True)
    return[database,cursor]