import socket  ## Inportação do socket que irá permitir as conexões

s = socket.socket() ## Atribui  "s" para o socket criar o objeto
host = socket.gethostname() ## host recebe  o endereço do programa
port = 8080  ## Definido a porta 8080, mas poderia ser qualquer outra que você queira.
s.bind((host, port))  ## Ligação do host e da porta com o socket
s.listen(1) ## Aqui ficamos ouvindo uma conexão de entrada
print(host) ## Imprime o endereço do servidor, que será usado pelo cliente se conectar ao servidor
print("Aguardando qualquer conexão de entrada ...")  ## Imprime a msn que aguarda uma conexão de entrada
conn, addr = s.accept()  ## Aceita todas as conexões
print(addr, "Se conectou ao servidor!") ## imprime o endereço do cliente que faz a conexão

## CRIANDO O ARQUIVO PARA TRANSFERÊNCIA
##Aqui o usuario entra com uma string informando o nome do arquivo que deseja e salva em filename
filename = input(str("Por favor, digite o nome do arquivo txt que deseja receber :   ")) 
file = open(filename , 'rb') ## Abre o arquivo no modo de leitura de bytes.
file_data = file.read(1024)
conn.send(file_data) ## Diz para a conexão enviar os dados ao cliente
print("Os dados foram transmitidos com sucesso!") ## Se os dados for transmitidos, imprime a msn de sucesso