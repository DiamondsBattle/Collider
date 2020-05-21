import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET : IPv6 and SOCK_STREAM : TCP
address = socket.gethostname()
address_port = 8888
s.bind((address, address_port))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    clientsocket.send(bytes(('Connected to a server : ' + str(address) + ':' + str(address_port)), 'utf-8'))