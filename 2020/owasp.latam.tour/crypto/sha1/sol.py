#!/usr/bin/env python
import hashlib, binascii

autores=["alguien","alguien_tw","jere","yehuju","perverthso","mrnox_","mateo"]
colores=["azul","rojo","amarillo","verde","violeta","negro"]
paises=["uruguay","argentina","brasil","paraguay","chile","bolivia","colombia","honduras","guatemala","mexico","ecuador","venezuela","costarica","peru"]
deportes=["atletismo", "remo", "badminton", "baloncesto", "boxeo", "canotaje", "ciclismo", "ecuestre", "esgrima", "futbol", "gimnasia", "halterofilia", "balonmano", "hockey", "judo", "natacion", "tenis", "vela", "voleibol"]

for a in autores:
	for c in colores:
		for p in paises:
			for d in deportes:
				h = hashlib.sha1()
				# flag format = owasp{autor_color_pais_deporte}
				flag = "owasp{%s_%s_%s_%s}" % (a,c,p,d)
				h.update(flag.encode('utf8'))
				if (h.hexdigest() == '0b27a389e4e8cef7ac346c932e45272156a72039'):
					print("Found it!")
					print("flag = {0}".format(flag))

