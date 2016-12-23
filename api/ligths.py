#!/usr/bin/python
#-*- coding:Utf-8 -*-

import sys,getopt
import re
from phue import Bridge

b = Bridge(sys.argv[2])
lang=sys.argv[1]

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
	try:
		if (b.get_light(light,'on')):
			b.set_light(light,'on',False)
		else:
			b.set_light(light,'on',True)
		status(light)
	except:
		print lbl[lang]['lamp'],lbl[lang]['unknow']
	

def status(light=1):
	try:
		status = b.get_light(light,'on')
	except:
		print lbl[lang]['lamp'],lbl[lang]['unknow']
	if (status):
		statusS=lbl[lang]['on']
	else:
		statusS=lbl[lang]['off']
			
	print lbl[lang]['lamp']+' '+light+' '+statusS
	return status
			
def router(arg):
	return {
		'toggle': toggle_lights,
		'status': status,
	}

if __name__ == "__main__":
	router = router (sys.argv)
	try:
		light=str(sys.argv[4]).capitalize()
		router[sys.argv[3]](light)
	except:
		print lbl[lang]['command'],' ',lbl[lang]['unknow']