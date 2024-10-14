from mysql.connector import Error
from datetime import datetime

def buscar_usuario_por_rfid(conn, codigo_rfid):
    try:
        with conn.cursor(dictionary=True) as cursor:
            query = "SELECT nome_aluno FROM alunos WHERE codigo_rfid = %s"
            cursor.execute(query, (codigo_rfid,))
            result = cursor.fetchall()  
        
        if result:
            print(f'Usuário encontrado: {result[0]["nome_aluno"]}')
            return result[0]['nome_aluno']
        else:
            print('Usuário não encontrado.')
            return None
    except Error as e:
        print(f'Erro ao buscar usuário: {e}')
        return None


def inserir_alunos(conn, codigo_rfid, nome):
    try:
        cursor = conn.cursor()
        data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        query = "INSERT INTO alunos (codigo_rfid, nome_aluno, data_hora) VALUES (%s, %s, %s)"  
        cursor.execute(query, (codigo_rfid, nome, data_hora))
        conn.commit()
        cursor.close()
        print('Leitura inserida com sucesso.')
    except Error as e:
        print(f'Erro ao inserir leitura: {e}')



