import socket
import threading
clientSocket = socket.socket()
clientSocket.connect(('127.0.0.1', 9123))
def sendMessage():
    while True:
        message = input("Введите сообщение: ")
        clientSocket.send(message.encode())

thread = threading.Thread(target=sendMessage)
thread.start()
while True:
    response = clientSocket.recv(1024)
    print("\nОтвет сервера: "+response.decode()+"\nВведите сообщение:")
