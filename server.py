
import socket
s = socket.socket()
print('Hi, I am server Socket Created by Rana Wahaj 21k-3281!')
s.bind(('localhost', 30498))
print('I am binding to localhost on port 30498')
s.listen(5)
print('Waiting for connection') 

c, addr = s.accept()
print('Yahoo! I got connected to', addr)
print("""Enter 'close' to exit""" )
strr = ''
while strr != 'close':
    strr = input('Enter Message -> ')
    if strr == 'close':
        continue
    strbyte = strr.encode('ascii')
    c.send(bytes(strbyte))
    strr = ''
    print('Client ->' + c.recv(1024).decode())
c.close()    

