"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Michal Šolc
email: solc.mich@seznam.cz
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

udaje = {
    "bob" : "123",
    "ann" : "pass123",
    "mike" : "password123",
    "liz" : "pass123"
}

uzivatel = input("Zadej uživatelské jméno: ")
heslo = input("Zadej heslo: ")
print(40 * "-")

if uzivatel in udaje and udaje[uzivatel] == heslo:
    print("Welcom to the app, ", uzivatel.upper(), '\n' "we have 3 texts to be analyzed.")
    print(40 * "-")
    index_textu = input("enter a number btw. 1 and 3 to select: ")
    print(40 * "-")
    if index_textu.isdigit():
      index_textu = int(index_textu)
      
      if index_textu == 3 or index_textu == 1 or index_textu ==2:

        text = TEXTS[index_textu -  1]
        slova = text.split()
        pocet_slov = len(slova)
        
        pocet_velkych = 0
        pocet_title = 0
        pocet_malych = 0
        pocet_cisel = 0
        soucet_cisel = 0
        for slovo in slova:
          if slovo.istitle():
            pocet_title += 1

          elif slovo.isupper():          
             pocet_velkych += 1
             
          elif slovo.islower():
            pocet_malych += 1
            
          elif slovo.isdigit():
            pocet_cisel += 1
            soucet_cisel += int(slovo)

        print("There are", pocet_slov, "words in the selected text.")
        print("There are",pocet_title, "titlecase words.")     
        print("There are", pocet_velkych, "uppercase words.") 
        print("There are", pocet_malych, "lowercase words.")  
        print("There are",pocet_cisel, "numeric strings.") 
        print("The sum of all the numbers:",soucet_cisel)
        print(40 * "-")  
        print("LEN|    OCCURENCES    |NR.")
        print(40 * "-")
        bez_dia = [slovo.strip(",.:;!?") for slovo in slova]
        delka_slov = [len(slovo) for slovo in bez_dia]
        sortr = sorted(delka_slov)
        max_delka = max(sortr)
        for delka in range(1, max_delka + 1):
          pocet_slov1 = delka_slov.count(delka)
          print("{:>3}|".format(delka) +(pocet_slov1 * "*") + (" " * (18-pocet_slov1)) + "|" + str(pocet_slov1))
                     
      
      else: 
        print("select correct number 1-2-3 !!")
    else:
     print("select correct number 1-2-3 !!")

else:
  print("incorrect username or password !!!")

        
print(40 * "-")