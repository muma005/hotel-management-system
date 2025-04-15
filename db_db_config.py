import mysql.connector

def get_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="yourpassword",
        database="hotel_management"
    )
    return connection