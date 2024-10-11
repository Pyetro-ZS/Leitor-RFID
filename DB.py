import mysql.connector
from mysql.connector import Error

def conectar_mysql():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="chamada_ceap",
            port="3306"
        )
        if conn.is_connected():
            print('Conectado ao MySQL com sucesso.')
            return conn
    except Error as e:
        print(f'Erro ao conectar ao MySQL: {e}')
        return None
