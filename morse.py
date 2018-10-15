import sys
alfabetoMorse = {
	
	"a" : ".-",
	"b" : "-...",
	"c" : "-.-.",
	"d" : "-..",
	"e" : ".",
	"f" : "..-.",
	"g" : "--.",
	"h" : "....",
	"i" : "..",
	"j" : ".---",
	"k" : "-.-",
	"l" : ".-..",
	"m" : "-.",
	"n" : "-.",
	"o" : "---",
	"p" : ".--." ,
	"q" : "--.-",
	"r" : ".-." ,
	"s" : "...", 
	"t" : "-",
	"u" : "..-",
	"v" : "...-", 
	"w" : ".--" ,
	"x" : "-..-",
	"y" : "-.--",
	"z" : "--..",
	"0" : "-----",
	"1" : ".----",
	"2" : "..---",
	"3" : "...--",
	"4" : "....-",
	"5" : ".....",
	"6" : "-....",
	"7" : "--...",
	"8" : "---..",
	"9" : "----.",
	"." : ".-.-.-",
	"," : "--..--",
	":" : "---...",
	"?" : "..--..",
	"=" : "-...-",
	"-" : "-....-",
	"(" : "-.--.",
	")" : "-.--.-",
	"/" : "-..-.",
	"@" : ".--.-.",
	"!" : "-.-.--",

	
}
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
				
				if parola != "":
					for i in parola:
						if i == " ":
							lp -= 1
							print("|", end="")
						for x in alfabetoMorse:
							if x == i:
								lp -= 1
								if lp == 0:
									print(alfabetoMorse[str(x)])
								else: 
									print(alfabetoMorse[str(x)], end="|")

				else: 
					sys.exit()

		elif z == "1":

			while True:
				print()
				print("inserisci il morse mettendo uno spazio tra le lettere e | tra le parole: (invio per uscire)")
				parola = input()
				p = " "
				if parola != "":
					for i in parola:
						if i == "|":
							print(" ", end="")
						else:
							if i != " ":
								p.join(i)	
								print(p, end="")
							#else:
								#for x in alfabetoMorse:
									#if x == p:
										#print(x, end="")	
									#else:
										#print("la lettera", p, "non esiste.")				
				else: 
					sys.exit()

		else:
			print("!!!inserisci 1 o 2!!!")
			break