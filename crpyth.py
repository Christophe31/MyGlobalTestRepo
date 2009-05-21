#/usr/bin/env python
import math
from random import random
from random import shuffle

class crpyt:
	def __init__(self):
		self.alphabets=["zaZetErRBYIUOFkvx_.+TGWCVHKJ132789hb6silmu/opLQMSgqjn,A5DPNX04cwdfy-=", \
					 "v+XWynzIu7TGU6D5ZHbE9cagkhof=FSRiMBteAd0qC2VlOrxKjw,NsQL-4p81.mY_P/J3", \
					 "iLU,DElSyZXBvWYP7w-_z0gj.rAK83q6R5fMe/QpTVxJnIch1OC+NouF2m=sdab9ktHG4"]
		self.randkey=""
		self.message=""
		self.key=""
		while question( "Quelle action voulez vous faire?", [ \
					["chiffrer un message", self.cryptloop] , \
					["dechiffrer un message",self.uncryptloop], \
					["quitter", quitter]])():
			pass


	def randkeygen(self):
		tmp=list(self.alphabets[0])
		shuffle(tmp)
		while self.alphabets[1].find(tmp[0])<5:
			shuffle(tmp)
		self.randkey="".join(tmp[0:self.alphabets[1].find(tmp[0])])

	def randkeyfind(self):
		self.randkey="".join(self.message[0:self.alphabets[1].find(tmp[0])])

	def keydefine(self):
		self.key=raw_input("quelle clef?")
		while len([i for i in self.key if i not in self.alphabets[0]])>0:
			self.key=raw_input("clef invalide: quelle clef?")

	def crypt(self):
		self.message=raw_input("quel message?")
		while len([i for i in self.key if i not in self.alphabets[0]])>0:
			self.key=raw_input("message invalide: quel message?")
		self.randkeygen()
		crypted=[l for l in self.randkey]
		for i,l in enumerate(self.message):
			crypted.append(self.alphabets[0][self.decal(l,self.key[i%len(self.key)],self.randkey[i%len(self.randkey)],i%len(self.alphabets))%len(self.alphabets[0])])
		print "".join(crypted)

	def uncrypt(self):
		self.message=raw_input("quel message?")
		while len([i for i in self.key if i not in self.alphabets[0]])>0:
			self.key=raw_input("message invalide: quel message?")
		self.randkeyfind()
		self.message=self.message[len(self.randkey)-1:]
		uncrypted=[]
		for i,l in enumerate(self.message):
			crypted.append(self.alphabets[0][self.decal(l,self.key[i%len(self.key)],self.randkey[i%len(self.randkey)],i%len(self.alphabets))%len(self.alphabets[0])])
		print "".join(crypted)

	def decal(self, letm,letk, letr, alph=0,mod=False):
		if mod:
			return self.alphabets[alph].find(letm)-self.alphabets[alph].find(letk)+self.alphabets[alph].find(letr)
		return self.alphabets[alph].find(letm)+self.alphabets[alph].find(letk)+self.alphabets[alph].find(letr)
	def cryptloop(self):
		self.keydefine()
		self.crypt()
		while question( "Quelle action voulez vous faire?", [ \
					["changer la clef", self.keydefine] , \
					["chiffrer un autre message",self.crypt], \
					["quitter", quitter]])():
			pass
		return True
	def uncryptloop(self):
		self.keydefine()
		self.uncrypt()
		while question( "Quelle action voulez vous faire?", [ \
					["changer la clef", self.keydefine] , \
					["chiffrer un autre message",self.uncrypt], \
					["quitter", quitter]])():
			pass
		return True


def color(string, code=1,background=False):
	"""colore une chaine de texte:
	0: gris, 1:rouge, 2:vert, 3:orange, 4:bleu, 5:violet, 6:bleu-ciel, 7:blanc """
	return "\033["+{False:"3" ,True:"4"}[background]+str(int(code)%10)+"m"+str(string)+"\033[m"

def question(Q, propositions, mode=False):
	"""pose la question Q (1er argument) avec les proposition (liste et 2eme argument), retourne le numereau de la reponce voulue"""
	t=0
	while t==0:
		print Q
		for p in propositions:
			t+=1
			print color(str(t), t), " -  ", p[0]
		t=1
		answer=raw_input('entrez une valeur numerique entiere \n')
		try: answer=int(answer)
		except: answer = -9
		if answer>=len(propositions) or answer<0:
			t=0
			print "Valeur en entree incorrecte"
	return propositions[answer-1][1]


def quitter():
	return False
###### Fin-Fonctions ######

###### MainLoop ######

crpyt()
