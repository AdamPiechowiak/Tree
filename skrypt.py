import string
plik = open("test.txt")

alfabet = string.ascii_lowercase

def obliczIloczyn1(tab, wierzcholek):
	
	wynik = []
	
	wynik.append(int(wierzcholek))
	for w2 in tab[1]:
		wynik.append(int(wierzcholek)*int(w2))
		for w3 in tab[2]:
			wynik.append(int(wierzcholek)*int(w2)*int(w3))
			for w4 in tab[3]:
				wynik.append(int(wierzcholek)*int(w2)*int(w3)*int(w4))
				for w5 in tab[4]:
					wynik.append(int(wierzcholek)*int(w2)*int(w3)*int(w4)*int(w5))
					for w6 in tab[5]:
						wynik.append(int(wierzcholek)*int(w2)*int(w3)*int(w4)*int(w5)*int(w6))
						for w7 in tab[6]:
							wynik.append(int(wierzcholek)*int(w2)*int(w3)*int(w4)*int(w5)*int(w6)*int(w7))
	
	
	return wynik
	
def zamien2(tab):
	
	wynik = []
	
	n = int(len(tab)/2)
	
	for i in range(n):
		wynik.append(tab[i*2+1])
		wynik.append(tab[i*2])
	wynik=wynik[::-1]
	
	return wynik
	
def zastap3(tab):
	
	wynik = []
	
	for liczba in tab:
		wynik.append(alfabet[liczba%26])
	
	return wynik

def liczba4(tab):
	
	tekst = "".join(tab)
	tekstbin = ""
	for znak in tekst:
		tekstbin = tekstbin+bin(ord(znak))[2:]
	a = int(tekstbin[:16],2)
	b = int(tekstbin[-16:],2)
	return a & b
	
def podziel5(liczba):
	
	tekst = str(liczba)
	n = int(len(tekst)/2)
	suma = 0
	for i in range(n):
		suma = suma + int(tekst[i*2:i*2+2])
	if(len(tekst)%2==1):
		suma= suma + int(tekst[-1])
	return suma
	
def oblicz15(tab,wierzcholek):
	c1 = obliczIloczyn1(tab,wierzcholek) 

	c2 = zamien2(c1)

	c3 = zastap3(c2)

	c4 = liczba4(c3)

	return podziel5(c4)
	
def operacja6(tab):
	tabstr = []
	for liczba in tab:
		tabstr.append(str(liczba))
	tekst = "".join(tabstr)
	print(tekst)
	w = pow(365,5) + pow(52,10) + pow(7,20) + 457981573849226022 - int(tekst)
	w = -w

	return w
	
def operacja7(liczba):
	tekst = str(liczba)
	n = int(len(tekst)/2)
	wynik = ""
	for i in range(n):
		wynik = wynik + alfabet[int(tekst[i*2:i*2+2])%26]
	if(len(tekst)%2==1):
		wynik = wynik + alfabet[int(tekst[-1])%26]
		
	return wynik
	
tab = []

for linia in plik:
	tab.append(linia[:-1].split(sep = '\t'))

tabw = []

for wierzcholek in tab[0]:
	c5 = oblicz15(tab,wierzcholek)
	tabw.append(c5)
	
c6 = operacja6(tabw)
print(c6)
c7 = operacja7(c6)

print(c7)
