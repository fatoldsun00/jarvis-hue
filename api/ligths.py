#!/usr/bin/python
#-*- coding:Utf-8 -*-
import sys#,getopt
#import re
from phue import Bridge
import json
import ast

b = Bridge(sys.argv[2])
lang=sys.argv[1]
TOSAY=""

lbl={
		'fr':{
			'on':'allumé',
			'off':'éteinte',
			'lamp':'lumière',
			'unknow':'inconnue',
			'error':'erreur',
			'command':'commande',
		},
		'en':{
			'on':'on',
			'off':'off',
			'lamp':'lamp',
			'unknow':'unknow',
			'error':'error',
			'command':'command',
		}
	}

def toggle_lights(light=1):
	global TOSAY
	try:
		if (b.get_light(light,'on')):
			b.set_light(light,'on',False)
		else:
			b.set_light(light,'on',True)
		status(light)
	except: 
		TOSAY= lbl[lang]['lamp']+" "+lbl[lang]['unknow']
		return TOSAY
		
def status(light=1):
	global TOSAY
	try:
		status = b.get_light(light,'on')
		if (status):
			statusS=lbl[lang]['on']
		else:
			statusS=lbl[lang]['off']
				
		TOSAY = lbl[lang]['lamp']+' '+light+' '+statusS
		
	except:
		TOSAY = lbl[lang]['lamp']+' '+lbl[lang]['unknow']	
	return TOSAY
			
def router(arg):
	return {
		'toggle': toggle_lights,
		'status': status,
	}

def main():
	global TOSAY
	routes = router(sys.argv)

	try:
		#Recherche dans le dico si le mot n'a pas ete mal traduit par le stt
		sys.argv[5]=ast.literal_eval(sys.argv[5])
		sys.argv[4] =sys.argv[5].get(sys.argv[4], sys.argv[4])
		light=str(sys.argv[4]).capitalize()
		routes[sys.argv[3]](light)
	except:
		TOSAY = lbl[lang]['command']+" "+lbl[lang]['unknow']
		
	print TOSAY

if __name__ == "__main__":
	main()
	