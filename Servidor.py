import socket
import threading
import time
import queue

# ==================== SERVIDOR ==================== #
def Cliente(pedido):
    with Lock:
        buffer.put(pedido)
        print("Cliente pediu um pedido: ", pedido)
        time.sleep(2)

def Cozinheiro():
    with Lock:
        comida = buffer.get()
        print("Cozinheiro preparando pedido: ", comida)
        time.sleep(2)
        


#Configura servidor e coloca no ar
Lock = threading.Lock()
buffer = queue.Queue(maxsize=5)
soquete_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soquete_servidor.bind(('localhost', 1024))
soquete_servidor.listen(5)
print("Servidor local rodando na porta 1024")

for i in range(20):
    cliente = soquete_servidor.accept()

