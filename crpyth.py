#/usr/bin/env python
import math
from random import random

alphabets=["zaZetErRBYIUOFkvx_.+TGWCVHKJ132789hb6silmu/opLQMSgqjn,A5DPNX04cwdfy-=",'v+XWynzIu7TGU6D5ZHbE9cagkhof=FSRiMBteAd0qC2VlOrxKjw,NsQL-4p81.mY_P/J3','iLU,DElSyZXBvWYP7w-_z0gj.rAK83q6R5fMe/QpTVxJnIch1OC+NouF2m=sdab9ktHG4']
randkey=""
message=""
key=""

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
def keydefine():
	key=raw_input("quelle clef?")
	while len([i for i in key if i not in alphabets[0]])>0:
		key=raw_input("quelle clef?")
def cryptloop():
	keydefine()
	crypt()
	while question( "Quelle action voulez vous faire?", [ \
				["changer la clef", keydefine] , \
				["chiffrer un autre message",crypt], \
				["quitter", quitter]])():
		pass
	return true

def uncryptloop():
	return true

def use_algo(texte, key, randkey):
	return


def quitter():
	return false
###### Fin-Fonctions ######

###### MainLoop ######
while question( "Quelle action voulez vous faire?", [ \
			["chiffrer un message", cryptloop] , \
			["dechiffrer un message",uncryptloop], \
			["quitter", quitter]])():
	pass

message=raw_input('message?')
k=int(raw_input('clef'))
mk=""
for i in [chr(ord(i)+k%256) for i in message]:
    mk+=i
print mk
