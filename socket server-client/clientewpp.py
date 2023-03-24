import socket
from threading import Thread


host = "127.0.0.1"
port = 8888

s = socket.socket()
print("Conectando em" , host , port)
s.connect((host, port))
print("Conectado")
name = input("Digite o seu nome: ")

def messages():
    while True:
        message = s.recv(1024).decode()
        print("\n" + message)

t = Thread(target=messages)
t.start()

while True:
    to_send =  input()
    to_send = f"{name}: {to_send}"
    s.send(to_send.encode())



