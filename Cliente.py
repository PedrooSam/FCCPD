import socket
import threading
            

# ==================== CLIENTE ==================== #

def enviar_pedido(i):
    #Criando conexão com servidor
    soquete_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soquete_cliente.connect(("localhost", 1024))

    #Envia o numero do pedido ao servidor
    soquete_cliente.sendall(f"{i}".encode())

    #Recebe confirmação do servidor
    print(soquete_cliente.recv(1024).decode())

    #Fecha a conexão
    soquete_cliente.close()


#lista para armazenar as threads dos clientes
clientes = []

#Looping para criação de vários clientes
for i in range(20):
    t = threading.Thread(target=enviar_pedido, args=(i,))
    clientes.append(t)
    t.start()

for t in clientes:
    t.join()