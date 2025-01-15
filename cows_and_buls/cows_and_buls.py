"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Michal Šolc
email: solc.mich@seznam.cz
"""
import random
print(
    f"Hi there!", "\n", "-"*47, "\n",
      "I've generated a random 4 digit number for you. ", "\n",
      "Let's play a bulls and cows game.", "\n", 47*"-", "\n",
      "Enter a number:", "\n", 47*"-", sep=""
      )     # program pozdraví uživatele a vypíše úvodní text
number = str(random.randint(1000,9999)) # vybere náhodně číslo - 4místné, které nezačíná 0
#print(number)
while True:
  if len(set(number)) < 4:  # počet číslic v čísle + set - množina bez duplicitních hodnot je menší než 4 číslice
    number = str(random.randint(1000,9999))
    #print(number)
    continue
  else:
    break

# hráč hádá číslo. Program jej upozorní,
#pokud zadá číslo kratší nebo delší než 4 čísla,
#pokud bude obsahovat duplicity, začínat nulou, příp. obsahovat nečíselné znaky

kolik_pokusu = 0  # vrací počet pokusů do uhodnutí čísla
while True:
  vloz_cislo = str(input(">>>"))
  if vloz_cislo.isdigit() == False: # pokud vstup není číslo
   print("zadej správné číslo")
   continue
  elif len(vloz_cislo) != 4: # pokud je vstup kratší nebo delší než 4 písmena
    print("zadej správné číslo")
    continue
  elif len(set(vloz_cislo)) < 4: # pokud jsou v číslu duplicitní hodnoty
    print("zadej správné číslo")
    continue
  elif vloz_cislo[0] == "0":  # pokud je první znak 0
    print("zadej správné číslo")
    continue
  elif number == vloz_cislo: # pokud se vstup rovná tajnému číslu - program se ukončí
    print("That's amazing!")
    kolik_pokusu += 1 # počítání pokusů do uhodnutí písma
    print(
        f"Correct, you've guessed the right number", "\n", 
        f"in {kolik_pokusu} guesses!", "\n",
        47*"-", sep=""
        ) 
    break
  else:
    while True:
      bulls = 0
      cows = 0
      
      for i in range(4):
        if vloz_cislo[i] == number[i]:  # cyklus testuje zda pozice vstupního čísla se shodují s tajnym číslem - vrací bull
          bulls += 1
        elif vloz_cislo[i] in number: # cyklus testuje zda je index vlozeneho čísla obsažené v tajném číslu - vrací cow
          cows += 1
      if bulls !=4:
        bull = "bull" if bulls == 1 else "bulls"  # podmínka vrací jednotné a množné číslo bull
        cow = "cow" if cows == 1 else "cows"  # podmínka vrací jednotné a množné číslo cow
        print(f"{cow} : {cows} and {bull} : {bulls}", sep = " ")
        kolik_pokusu += 1 # počítá počet cyklů - kolik pokusů
        break
      continue
