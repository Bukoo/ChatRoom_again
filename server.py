import socket
import threading
import time 
                                                           
def tcplink(sock, addr):
    print 'Accept new connection from %s:%s...' % addr
    sock.send('Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if data == 'exit' or not data:
            break
        print data
        sock.send('Hello, %s!' % data)
    sock.close()
    print 'Connection from %s:%s closed.' % addr

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9999))
s.listen(5)
print 'Waiting for connection...'
socks = {}
while True:
    sock, addr = s.accept()
    socks[sock] = addr
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()