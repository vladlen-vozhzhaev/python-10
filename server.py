import socket
import threading
serverSocket = socket.socket()
serverSocket.bind(('127.0.0.1', 9123))
serverSocket.listen(1)
print("Сервер запущен")
sockets = []
def chatting(clientSocket):
    while True:
        data = clientSocket.recv(1024)
        print(f"Сообщение от клиента: {data.decode()}")
        for client in sockets:
            client.send(data)

while True:
    print("ожидает подключение клиента...")
    clientSocket, clientAddr = serverSocket.accept()
    sockets.append(clientSocket)
    print(f"Клиент подключился {clientAddr}")
    thread = threading.Thread(target=chatting, args=(clientSocket,))
    thread.start()


