
import socket
s = socket.socket() 
print('Hi i am client Socket Created by Rana Wahaj 21k-3281!')
s.connect(('localhost', 30498)) 
print('waitng for server to connect')
print("You are connected with server, send messages to server")
print("""Enter 'close' to exit""" )
strr = ''
while strr != 'close':
    print('Server->' + s.recv(1024).decode())
    strr = input('Enter Message -> ')
    if strr == 'close':
        continue
    strrbyte = strr.encode('ascii')
    s.send(bytes(strrbyte))
    strr = ''
print('client is signing off')
s.close()

