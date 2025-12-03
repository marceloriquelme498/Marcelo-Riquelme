import mysql.connector 
from mysql.connector import Error 
 
def get_db_connection(): 
    try: 
        connection = mysql.connector.connect( 
            host='localhost', 
            port=3307, 
            user='root', 
            password='root123', 
            database='ganado_db' 
        ) 
        return connection 
    except Error as e: 
        print(f"Error de conexión: {e}") 
        return None 
