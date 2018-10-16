import sys
from obj import alfabetoMorse, morseAlfabeto

while True:
	while True:
		print("morse-alfabeto(1) o alabeto-morse(2)?")
		z = input()
		if z == "2":
			while True:
				print()
				print("inserisci la lettera/parola/frase: (invio per uscire)")
				parola = input()
				lp = len(parola)
				p = ""
				if parola != "":
					for i in parola:
						if i == " ":
							lp -= 1
							p += "|"
						for x in alfabetoMorse:
							if x == i:
								lp -= 1
								if lp == 0:
									p += alfabetoMorse[str(x)]
								else: 
									p += alfabetoMorse[str(x)] + "|"
					print(p)
				else: 
					sys.exit()

		elif z == "1":
			while True:
				print()
				print("inserisci il morse mettendo una | tra le lettere e || tra le parole: (invio per uscire)")
				parola = input()
				p = ""
				if parola != "":
					parola = parola.split("|")
					for i in parola:
						if i == "":
							p += " "
						else:
							p += morseAlfabeto[i]
					print(p)
				else: 
					sys.exit()
		else:
			print("!!!inserisci 1 o 2!!!")
			break