from datetime import datetime
import os
import socket
import threading
import time

#Topo com informações do projeto prático
textoSaudacao = [
    '*' * 100,
    f"{'🐍 bem vindo ao chat p2p com sockets tcp e threads' .upper():^100}",
    f"{'🔌 protocolos e interconecção de redes de computadores' .upper():^100}",
    '*' * 100
]

#Uso da função .join para concatenar elementos da lista (textoSadudacao)
print('\n'.join(textoSaudacao))
time.sleep(2)

#Portas disponiveis simuladas
portas_disponiveis = [5000, 5001, 5002, 5003, 5004]

#Coleta informações dos usuários
solicita_usuario = [
    f"{'🔌 Abaixo informe os dados para realizar a conexão'.center(100)}"
]

#Exibindo a mensagem de boas vindas antes das portas disponíveis
print('\n'.join(solicita_usuario))

#Exibindo as portas simuladas disponíveis
print("\n🧷 Portas disponíveis para uso na conexão: ")

for porta in portas_disponiveis:
  print(f" 🔌- {porta}")

#Solicita informações para conexão do usuário com validação da porta
usuario = input("\n👤 Nome do usuário: ")

while True:
    try:
        porta_usuario = int(input(f"👤 {usuario}, escolha uma porta da lista: "))
        if porta_usuario in portas_disponiveis:
            break
        else:
            print("❌ Porta inválida. Tente novamente.")
    except ValueError:
        print("⚠️ Por favor, insira um número válido.")

#Exibe a informação do usuário e porta conectada
print(f"\n👤 Usuário {usuario} escolheu a porta 🔌 {porta_usuario}.")

# Inicializa conexões
conexoes = []

#Peers conectados
todos_peers = [('localhost', p) for p in portas_disponiveis if p != porta_usuario]

#Criando servidor e tornando acessível á todos
servidor = None

#Inicando execução do servidor TCP
def executando():
  global servidor
  servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  servidor.bind(('localhost', porta_usuario))
  servidor.listen(10)
  print(f"[👤{usuario}] Executando em localhost: 🔌 {porta_usuario} ...")
  time.sleep(2)
  while True:
    try:
      conn, addr = servidor.accept()
      conexoes.append(conn)
      threading.Thread(target=recebimento_mensagens, args=(conn,), daemon=True).start()
      registro_logs(f"[ENTRADA USR] Conexão recebida de {addr}")

    except OSError:
      break #Fecha servidor e sai do loop

#Iniciou a função de recebimento de mensagens
def recebimento_mensagens(conn):
  while True:
    try:
      dados = conn.recv(1024)
      if not dados:
        break
      mensagem = dados.decode('utf-8')
      # Exibe a mensagem recebida (uma vez)
      print("\n" + mensagem)
      #Registro de logs de mensagens recebidas
      registro_logs(f"[MSG RECEBIDA] {mensagem}")

    except ConnectionResetError:
      break

#Conecção dos peer e exibição das conexões ativas
def conectar_peers():
  while True:
    for ip, porta in todos_peers:
      try:
        if any(conn.getpeername()[1] == porta for conn in conexoes if isinstance(conn, socket.socket)):
          continue
      except OSError:
        pass

      try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, porta))
        conexoes.append(s)
        print(f"\t✅ [{usuario}] Conectado com sucesso!\n\tIP DE PEER: [{ip}]\n\tPORTA DE CONEXÃO: [{porta}]")
        print(f"\t👋 Olá,👤 {usuario}! Seja bem-vindo ao chat.")
        print(f"\t🔌[INFO] Total de conexões ativas: {len(conexoes)}")
        registro_logs(f"[USR CONECTADO] Conectado ao peer na porta {porta}")

      except:
           pass

    time.sleep(5)

#Bloco de função de envio de mensagens
def enviar_mensagens(msg):
  for conn in list(conexoes):
      try:
        conn.send(f"{usuario}: {msg} \n".encode('utf-8'))
        registro_logs(f"[MSG ENVIADA] {usuario}: {msg}")

      except:
          try:
              conexoes.remove(conn)
          except:
              pass

#Funçaõ que o arquivo Registro de logs
def registro_logs(mensagem):
    timestamp = datetime.now().strftime("[%d/%m/%Y %H:%M:%S]")
    linha = f"{timestamp} : {mensagem}\n"
    with open("logs_chat.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{timestamp} : {mensagem}\n")

#Informa quando usuário sai do chat
def avisar_saida_usuario():
  mensagem_saida = f"🔚{usuario} saiu do chat!"
  #registra a saída no log
  registro_logs(f"[INF SAIDA] {usuario}, encerrou o chat.")

  for conn in list(conexoes):
    try:
      conn.send(mensagem_saida.encode('utf-8'))
    except:
      pass

# Fecha as conexões com os peers
def encerrar_conexao():
  for conn in list(conexoes):
      try:
          conn.close()
      except:
          pass

# Função para encerrar corretamente o programa
def finalizar():
    print("🔚 Encerrando o chat...")
    avisar_saida_usuario()
    time.sleep(2)  # aguarda enviar mensagens e gravar logs
    #se usuário atual encerrar o chat, exibe a mensagem
    texto_final = ['*' * 100,
                  f"👤 {usuario}, ⚠️ chat encerrado, 🗃️ consulte o log para informações das conexões.",
                  '*' * 100 ]
    print("📁 Todos os eventos foram registrados em 'logs_chat.txt'.")
    print("🗃️ Diretório atual log:", os.getcwd())
    print('\n'.join(texto_final))
    time.sleep(2)
    if servidor:
        try:
            servidor.close()
        except:
            pass

    encerrar_conexao()

#Executando as Threads em segundo plano
threading.Thread(target=executando, daemon=True).start()
threading.Thread(target=conectar_peers, daemon=True).start()

#Loop principal protegido para garantir encerramento
try:
    while True:
        texto = input()
        if texto.strip().lower() == "sair":
            break
        enviar_mensagens(texto)
        print(f"(Você) 💬: {texto}")
finally:
    finalizar()