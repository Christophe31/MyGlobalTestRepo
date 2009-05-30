#!/usr/bin/env python
#! -*- coding:utf8 -*-
#
#       MServ.py
#
#       2009 Narbonne Christophe <cricri.nanar@laposte.net>

from socket import socket

class Serv:
	def __init__(self):
		self.pseudo=raw_input("Quel pseudo?")
		self.sock=socket()
		self.sock((self.serverIp,self.serverPort))
		self.sock.send(self.pseudo)
