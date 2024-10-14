import keyboard
from scanner import buscar_usuario_por_rfid, inserir_alunos
from db import conectar_mysql

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

def main():
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

if __name__ == '__main__':
    main()