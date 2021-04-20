import socket  ## Inportação do socket que irá permitir as conexões

s = socket.socket()  ## Atribui  "s" para o socket criar o objeto
host = input(str("Digite o endereço de host do remetente :  ")) ## Aqui o usuario entra com uma string com o endereço do servidor
port = 8080  ## Fornece a porta para conexão
s.connect((host, port))  ## Conecta as portas do host fornecidas
print("Conectado...")  ## Se estiver tudo ok com a conexão é imprime a msn Conectado...

## CRIANDO O ARQUIVO RECEBIDO
## Aqui criamos um nome qualquer para receber os dados do arquivo do servidor, O nome precisa ter o mesmo tipo por exemplo: txt 
filename = input(str("Digite um nome para o arquivo de entrada :  "))
file = open(filename, 'wb') ## Abre o arquivo no modo de escrita.
file_data = s.recv(1024)
file.write(file_data)  ## Escreve os dados recebidos no arquivo.
file.close()  ## Fecha o arquivo.
print("O arquivo foi recebido com sucesso!")  ## Se a transferencia for bem sucedida, imprime a msn de sucesso.