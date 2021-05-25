import socket
host = 'localhost'
port = 8000
addr = (host,port)
serv_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serv_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
serv_socket.bind(addr)
serv_socket.listen(10)
print('Aguardando conexão...')
con, cliente = serv_socket.accept()
print('Conectado!')
print('Aguardando mensagem...')

enviar = ''

while(enviar != 'sair'):
    recebe = con.recv(1024)
    print('Mensagem recebida:' + recebe.decode())
    enviar = input('Digite uma mensagem para enviar ao cliente:')
    con.send(enviar.encode())

print('Saindo...')
serv_socket.close()