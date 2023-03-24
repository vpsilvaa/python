import socket
from threading import Thread

host = "localhost"
port = 8888 
client = set()
s = socket.socket()
s.bind((host, port))
s.listen(5)
print("Escutando em" , host , port)

def clients(cs):
    while True:
        try:
            message = cs.recv(1024).decode()
        except Exception as e:
            print("Erro!")
            client.remove(cs)

        for client_aux in client:
            client_aux.send(message.encode())

while True:
    client_aux, address = s.accept()
    print(address , "conectado.")
    client.add(client_aux)
    t = Thread(target=clients, args=(client_aux,))
    t.start()



    