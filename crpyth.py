#! /usr/bin/env python
# -*- coding:utf-8 -*-
# coded with Tab = 5 spaces

import math
from random import random
from random import shuffle
from sys import argv
print argv
class crpyt:
	def __init__(self):
		self.alphabets=["zaZetErRBYIUOFkvx_.+TGWCVHKJ132789hb6silmu/opLQMSgqjn,A5DPNX04cwdfy-=", \
					 "v+XWynzIu7TGU6D5ZHbE9cagkhof=FSRiMBteAd0qC2VlOrxKjw,NsQL-4p81.mY_P/J3", \
					 "iLU,DElSyZXBvWYP7w-_z0gj.rAK83q6R5fMe/QpTVxJnIch1OC+NouF2m=sdab9ktHG4"]
		self.randkey=""
		self.message=""
		self.key=""
		self.CKs=["","","","",""]
		a=-1
		self.key=raw_input("quelle clef?")
		while len([i for i in self.key if i not in self.alphabets[0]])>0:
			self.key=raw_input("clef invalide: quelle clef?")
		while a!=4:
			a=question( "Quelle action voulez vous faire?", [		\
					"Chiffrer un message" ,					\
					"Dechiffrer un message",					\
					"Changer la clef",						\
					"Quitter"])
			if a < 3:
				self.message=raw_input("quel message?")
				while len([i for i in self.message if i not in self.alphabets[0]+" "])>0:
					self.message=raw_input("message invalide: quel message?")
				self.message=self.message.replace(" ","_")
			if a==1:
				self.crypt(False)
			elif a==2:
				self.crypt(True)
			elif a==3:
				self.key=raw_input("quelle clef?")
				while len([i for i in self.key if i not in self.alphabets[0]])>0:
					self.key=raw_input("clef invalide: quelle clef?")

	def randkeym(self, find=False):
		"""génère ou trouve les clefs aléatoires"""
		if find:
			self.randkey="".join(self.message[0:self.alphabets[1].find(self.message[0])])
			self.message=self.message[len(self.randkey):]
		else:
			tmp=list(self.alphabets[0])
			shuffle(tmp)
			while self.alphabets[1].find(tmp[0])<5:
				shuffle(tmp)
			self.randkey="".join(tmp[0:self.alphabets[1].find(tmp[0])])
		for i in range(len(self.CKs)):
			self.CKs[i]=self.randkey[i]

	def crypt(self, uncrypt=False):
		"""fonction qui chiffre et déchiffre"""
		self.randkeym(uncrypt)
		result =	[
					self.alphabets[i%len(self.alphabets)]			\
					[										\
						self.decal							\
						(									\
							l,								\
							self.key[i%len(self.key)],			\
							self.randkey[i%len(self.randkey)], 	\
							self.getCK(i),						\
							self.getCK(int(782*math.cos(i))),		\
							i%len(self.alphabets),				\
							uncrypt							\
						)									\
						%len(self.alphabets[0])					\
					]										\
					for i,l in enumerate(self.message)				\
				]
		print {False:self.randkey+"".join(result) ,True:"".join(result).replace('_',' ')}[uncrypt]

	def getCK(self, i):
		return self.CKs[i%len(self.CKs)][i%len(self.CKs[i%len(self.CKs)])]

	def decal(self, letm,letk, letr, letc, letc2 ,alph=0,uncrypt=False):
		"""détermine le décalage à un index donné et retourne le nouvel index """
		val=self.alphabets[alph].find(letk)+self.alphabets[alph].find(letr)+self.alphabets[alph].find(letc)+self.alphabets[alph].find(letc2)
		self.CKs[int(math.sqrt(val)**3)%len(self.CKs)]+=self.alphabets[alph][int(6491*math.sin(val))%len(self.alphabets[alph])]
		if uncrypt:
			return self.alphabets[alph].find(letm)-val
		return self.alphabets[alph].find(letm)+val

def color(string, code=1,background=False):
	"""colore une chaine de texte:
	0: gris, 1:rouge, 2:vert, 3:orange, 4:bleu, 5:violet, 6:bleu-ciel, 7:blanc """
	return "\033["+{False:"3" ,True:"4"}[background]+str(int(code)%10)+"m"+str(string)+"\033[m"

def question(Q, propositions, mode=False):
	"""pose la question Q avec les proposition, retourne le numereau de la reponce voulue"""
	t=0
	while t==0:
		print Q
		for p in propositions:
			t+=1
			print color(str(t), t), " -  ", p
		t=1
		answer=raw_input('entrez une valeur numerique entiere \n')
		try: answer=int(answer)
		except: answer = -9
		if answer>=len(propositions) or answer<0:
			t=0
			print "Valeur en entree incorrecte"
	return answer

def quitter():
	return False

crpyt()
