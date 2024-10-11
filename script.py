import mysql.connector
from mysql.connector import Error
from datetime import datetime
import keyboard

def conectar_mysql():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="py",
            password="1234",
            database="chamada_ceap",
            port="3307"  
        )
        if conn.is_connected():
            print('Conectado ao MySQL com sucesso.')
            return conn
    except Error as e:
        print(f'Erro ao conectar ao MySQL: {e}')
        return None

def buscar_usuario_por_rfid(conn, codigo_rfid):
    try:
        cursor = conn.cursor(dictionary=True)
        query = "SELECT nome_aluno FROM alunos WHERE codigo_rfid = %s"
        cursor.execute(query, (codigo_rfid,))
        result = cursor.fetchone()
        cursor.close()
        if result:
            print(f'Usuário encontrado: {result["nome_aluno"]}')
        else:
            print('Usuário não encontrado.')
        return result['nome_aluno'] if result else None
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

def processar_rfid(conn, codigo_rfid):
    print(f'Processando código RFID: {codigo_rfid}')
    nome = buscar_usuario_por_rfid(conn, codigo_rfid)
    if nome:
        inserir_alunos(conn, codigo_rfid, nome)
        print(f'Leitura registrada: {codigo_rfid} - {nome}')
    else:
        print(f'Usuário não encontrado para o código RFID: {codigo_rfid}')

def capturar_rfid():
    codigo_rfid = ""
    print("Aproxime o cartão RFID do leitor...")
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == 'enter':
                break
            else:
                codigo_rfid += event.name
    print(f'Código RFID capturado: {codigo_rfid}')
    return codigo_rfid

if __name__ == '__main__':
    conn = conectar_mysql()
    if conn:
        try:
            while True:
                codigo_rfid = capturar_rfid()
                processar_rfid(conn, codigo_rfid)
        except KeyboardInterrupt:
            print("Encerrando...")
        finally:
            conn.close()
            print("Conexão MySQL encerrada.")
