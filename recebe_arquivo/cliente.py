import socket

s = socket.socket()
host = input(str("Digite o endereço de host do remetente :  "))
port = 8080
s.connect((host, port))
print("Conectado...")

filename = input(str("Digite um nome de arquivo para o arquivo de entrada :  "))
file = open(filename, 'wb')
file_data = s.recv(1024)
file.write(file_data)
file.close()
print("O arquivo foi recebido com sucesso!")