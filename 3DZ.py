# серверная часть
import socket
HOST = '127.0.0.1'
PORT = 7777
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print 'Connected client'
while True:
 data = conn.recv(10000)
 if not data:
 break
 else:
 print 'Received[2]: ', data
 conn.send(data)
 print 'Send[3]: ', data
conn.close()

# клиентская часть
import socket
HOST = '127.0.0.1'
PORT = 7777
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
data = 'Hello world'
s.send(data)
print 'Send[1]: ', data
data = s.recv(10000)
s.close()
print 'Received[4]: ', data