import sys
from dict import alfabetoMorse, morseAlfabeto

while True:
	while True:
		print("morse-alfabeto(1) o alabeto-morse(2)? (invio per uscire)")
		z = input()
		if z == "":
			sys.exit()
		if z == "2":
			while True:
				print()
				print("inserisci la lettera/parola/frase: (invio per toranre)")
				parola = input()
				lp = len(parola)
				p = ""
				if parola != "":
					for i in parola:
						if i not in alfabetoMorse and i != " ":
							print("Il carattere:", i, " non esiste :(")
							break
						elif i == " ":
							lp -= 1
							p += "|"
						for x in alfabetoMorse:
							if x == i:
								lp -= 1
								if lp == 0:
									p += alfabetoMorse[x]
								else: 
									p += alfabetoMorse[x] + "|"
					print(p)
				else: 
					break

		elif z == "1":
			while True:
				print()
				print("inserisci il morse mettendo una | tra le lettere e || tra le parole: (invio per toranre)")
				parola = input()
				p = ""
				if parola != "":
					parola = parola.split("|")
					for i in parola:
						if i not in morseAlfabeto and i != "":
							print("Il carattere:", i, " non esiste :(")
							break	
						if i == "":
							p += " "
						else:
							p += morseAlfabeto[i]
					print(p)
				else: 
					break
		else:
			print("!!!inserisci 1 o 2!!!")
			break
