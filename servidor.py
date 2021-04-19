import socket

s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host, port))
s.listen(1)
print(host)
print("Aguardando qualquer conexão de entrada ...")
conn, addr = s.accept()
print(addr, "Se conectou ao servidor!")

filename = input(str("Por favor, digite o nome do arquivo :  "))
file = open(filename , 'rb')
file_data = file.read(1024)
conn.send(file_data)
print("Os dados foram transmitidos com sucesso!")