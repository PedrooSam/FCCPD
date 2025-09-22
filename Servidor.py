import socket
import threading
import time
import queue

# ==================== SERVIDOR ==================== #

#Função do cliente (produtor)
def Cliente(cliente, endereco):
    with cliente:
        #Recebe o número do pedido passado pelo cliente
        pedido = cliente.recv(1024).decode()

        if not pedido:
            print(f"Cliente {endereco} não enviou nenhum pedido.")
            return

        with lock:
            buffer.put(pedido)
            print(f"Cliente {endereco} fez um pedido: {pedido}")
            cliente.send("Seu pedido foi adicionado à fila.".encode())
            time.sleep(2)



#Função do cozinheiro (consumidor)
def Cozinheiro(cozinheiro):
    while True:
        pedido = buffer.get()
        print(f"Cozinheiro {cozinheiro} preparando pedido: {pedido}")
        time.sleep(2)
        print(f"Cozinheiro {cozinheiro} terminou o pedido: {pedido}")
        buffer.task_done()
        

#Configurações iniciais para o projeto
lock = threading.Lock()
buffer = queue.Queue(maxsize=5)

#Configura servidor e coloca no ar
soquete_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soquete_servidor.bind(('localhost', 1024))
soquete_servidor.listen(5)
print("Servidor local rodando na porta 1024")

#Criação dos cozinheiros
for i in range(2):
    cozinheiro = i+1
    threading.Thread(target=Cozinheiro, args=(cozinheiro,), daemon=True).start()

#Loop para aceitação de clientes
while True:
    #aceita conexão com cliente
    cliente, endereco = soquete_servidor.accept()

    #Inicia uma thread para o cliente
    threading.Thread(target=Cliente, args=(cliente, endereco), daemon=True).start()