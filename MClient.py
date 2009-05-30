#!/usr/bin/env python
#! -*- coding:utf8 -*-
#
#       MClient.py
#
#       Narbonne Christophe <cricri.nanar@laposte.net>

from socket import socket
class Client:
	def __init__(self):
		self.serverIp=raw_input("Quelle IP?")
		self.serverPort=int(raw_input("Quel port?"))
		self.pseudo=raw_input("Quel pseudo?")
		self.sock=socket()
		self.sock((self.serverIp,self.serverPort))
		self.sock.send(self.pseudo)


Client()
