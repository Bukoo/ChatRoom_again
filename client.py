import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))
print s.recv(1024)
while True:
	data = raw_input("input anything")
	if data == "exit":
		s.close()
		break
	else:
		s.send(data)
		print s.recv(1024)
