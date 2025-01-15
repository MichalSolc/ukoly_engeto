"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Michal Šolc
email: solc.mich@seznam.cz
"""
from ast import While
zaklad1 = ["+","-","-","-","+","-","-","-","+","-","-","-","+"]
list1 = ["|"," "," "," ","|"," "," "," ","|"," "," "," ","|"]
list2 = ["|"," "," "," ","|"," "," "," ","|"," "," "," ","|"]
list3 = ["|"," "," "," ","|"," "," "," ","|"," "," "," ","|"]

def ctverec():
  for z in zaklad1:
    print(z, end = " ")
  print()
  for i in list1:
    print(i, end = " ")
  print()
  for z in zaklad1:
    print(z, end = " ")
  print()
  for ii in list2:
    print(ii, end = " ")
  print()
  for z in zaklad1:
    print(z, end = " ")
  print()
  for iii in list3:
    print(iii, end = " ")
  print()
  for z in zaklad1:
    print(z, end = " ")
  print()

def player_x():
  while True:
    vstup = input("PLAYER X | Please enter your move number: ")
    print(44*"=")
    if vstup == "1" and list1[2] == " ":
      list1.pop(2)
      list1.insert(2,"X")
      ctverec()
    elif vstup == "2" and list1[6] == " ":
      list1.pop(6)
      list1.insert(6,"X")
      ctverec()
    elif vstup == "3" and list1[10] == " ":
      list1.pop(10)
      list1.insert(10,"X")
      ctverec()
    elif vstup == "4" and list2[2] == " ":
      list2.pop(2)
      list2.insert(2,"X")
      ctverec()
    elif vstup == "5" and list2[6] == " ":
      list2.pop(6)
      list2.insert(6,"X")
      ctverec()
    elif vstup == "6" and list2[10] == " ":
      list2.pop(10)
      list2.insert(10,"X")
      ctverec()
    elif vstup == "7" and list3[2] == " ":
      list3.pop(2)
      list3.insert(2,"X")
      ctverec()
    elif vstup == "8" and list3[6] == " ":
      list3.pop(6)
      list3.insert(6,"X")
      ctverec()
    elif vstup == "9" and list3[10] == " ":
      list3.pop(10)
      list3.insert(10,"X")
      ctverec()
    else:
      print("wrong input")
      continue
    break
def player_o():
  while True:
    vstup = input("PLAYER 0 | Please enter your move number: ")
    print(44*"=")
    if vstup == "1" and list1[2] == " ":
      list1.pop(2)
      list1.insert(2,"O")
      ctverec()
    elif vstup == "2" and list1[6] == " ":
      list1.pop(6)
      list1.insert(6,"O")
      ctverec()
    elif vstup == "3" and list1[10] == " ":
      list1.pop(10)
      list1.insert(10,"O")
      ctverec()
    elif vstup == "4" and list2[2] == " ":
      list2.pop(2)
      list2.insert(2,"O")
      ctverec()
    elif vstup == "5" and list2[6] == " ":
      list2.pop(6)
      list2.insert(6,"O")
      ctverec()
    elif vstup == "6" and list2[10] == " ":
      list2.pop(10)
      list2.insert(10,"O")
      ctverec()
    elif vstup == "7" and list3[2] == " ":
      list3.pop(2)
      list3.insert(2,"O")
      ctverec()
    elif vstup == "8" and list3[6] == " ":
      list3.pop(6)
      list3.insert(6,"O")
      ctverec()
    elif vstup == "9" and list3[10] == " ":
      list3.pop(10)
      list3.insert(10,"O")
      ctverec()
    else:
      print("wrong input")
      continue
    break


print(f"""Welcome to Tic Tac Toe
============================================
GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row
============================================
Let's start the game!
--------------------------------------------
""")
ctverec()
while True:

  print(44*"=")
  player_x()
  if list1[2] == "X" and list1[6] == "X" and list1[10] == "X":
    print("PLAYER X WINS")
    break
  elif list2[2] == "X" and list2[6] == "X" and list2[10] == "X":
    print("PLAYER X WINS")
    break
  elif list3[2] == "X" and list3[6] == "X" and list3[10] == "X":
    print("PLAYER X WINS")
    break
  elif list1[2] == "X" and list2[2] == "X" and list3[2] == "X":
    print("PLAYER X WINS")
    break
  elif list1[6] == "X" and list2[6] == "X" and list3[6] == "X":
    print("PLAYER X WINS")
    break
  elif list1[10] == "X" and list2[10] == "X" and list3[10] == "X":
    print("PLAYER X WINS")
    break
  elif  list1[2] == "X" and list2[6] == "X" and list3[10] == "X":
    print("PLAYER X WINS")
    break
  elif list1[10] == "X" and list2[6] == "X" and list3[2] == "X":
    print("PLAYER X WINS")
    break
  kolo = 0
  for znak in list1 + list2 + list3:
    if znak == "X" or znak == "O":
      kolo += 1
  if kolo == 9:
    print("DRAW")
    break

  print(44*"=")
  player_o()
  if list1[2] == "O" and list1[6] == "O" and list1[10] == "O":
    print("PLAYER O WINS")
    break
  elif list2[2] == "O" and list2[6] == "O" and list2[10] == "O":
    print("PLAYER O WINS")
    break
  elif list3[2] == "O" and list3[6] == "O" and list3[10] == "O":
    print("PLAYER O WINS")
    break
  elif list1[2] == "O" and list2[2] == "O" and list3[2] == "O":
    print("PLAYER O WINS")
    break
  elif list1[6] == "O" and list2[6] == "O" and list3[6] == "O":
    print("PLAYER O WINS")
    break
  elif list1[10] == "O" and list2[10] == "O" and list3[10] == "O":
    print("PLAYER O WINS")
    break
  elif  list1[2] == "O" and list2[6] == "O" and list3[10] == "O":
    print("PLAYER O WINS")
    break
  elif list1[10] == "O" and list2[6] == "O" and list3[2] == "O":
    print("PLAYER O WINS")
    break
  kolo = 0
  for znak in list1 + list2 + list3:
    if znak == "X" or znak == "O":
      kolo += 1
  if kolo == 9:
    print("DRAW")
    break

