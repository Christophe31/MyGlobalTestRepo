#!/usr/bin/env python
#! -*- coding:utf8 -*-
#
#       MServ.py
#
#       2009 Narbonne Christophe <cricri.nanar@laposte.net>

import socket

class Serv:
	def __init__(self):
		self.serverPort=int(raw_input("Quel port?"))
		self.pseudo=raw_input("Quel pseudo?")
		self.sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.bind(("",self.serverPort))
		self.sock.listen(8)
		self.conn, self.addr = self.sock.accept()
		while True:
			data = conn.recv(1024)
			if not data: break
			conn.send(data)
Serv()
