import socket

serverSocket = socket.socket()
serverSocket.bind(('127.0.0.1', 9123))
serverSocket.listen(1)
print("Сервер запущен и ожидает подключение клиента...")
clientSocket, clientAddr = serverSocket.accept()
print(f"Клиент подключился {clientAddr}")

while True:
    data = clientSocket.recv(1024)
    print(f"Сообщение от клиента: {data.decode()}")
    clientSocket.send(data.decode().upper().encode())