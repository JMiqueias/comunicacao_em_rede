import socket
ip = 'localhost'
port = 8000
addr = (ip,port)
cliente_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cliente_socket.connect(addr)

mensagem = ''

while(mensagem != 'sair'):
    mensagem = input('Digite uma mensagem para enviar ao servidor:')
    cliente_socket.send(mensagem.encode())
    #print('Mensagem enviada!')
    print('Mensagem recebida:' + cliente_socket.recv(1024).decode())

print('Saindo...')
cliente_socket.close()