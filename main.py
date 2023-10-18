"""
Kérj be két számot a felhasználótól (main.py)
Írj eljárást
    szamok néven, (ciklusok.py)
    melynek a paraméterek a felhasználó által megadott két szám
    és
    az eljárás kiírja a számokat ezen két paraméter között.
"""
import ciklusok


szam1: int = int(input("Adj meg egy számot!"))
szam2: int = int(input("Adj meg még egy számot!"))

ciklusok.szamok(szam1,szam2)