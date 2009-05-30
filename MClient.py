#!/usr/bin/env python
#! -*- coding:utf8 -*-
#
#       MClient.py
#
#       Narbonne Christophe <cricri.nanar@laposte.net>

import socket
class Client:
	def __init__(self):
		self.serverIp=raw_input("Quelle IP?")
		self.serverPort=int(raw_input("Quel port?"))
		self.pseudo=raw_input("Quel pseudo?")
		self.sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.bind((self.serverIp,self.serverPort))
		self.sock.send(self.pseudo)
		self.sock.close()


Client()
