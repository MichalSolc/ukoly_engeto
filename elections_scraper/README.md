Skript dostane URL stránky volebních výsledků.
Stáhne hlavní stránku a extrahuje základní údaje o volebních výsledcích a seznamu politických stran.
Pro každou politickou stranu (získanou z hlavní stránky) stáhne podrobné údaje o počtu hlasů z jiné stránky.
Výsledky (včetně počtu hlasů pro jednotlivé strany) jsou uloženy do CSV souboru, který obsahuje:
Kód obce, Lokalitu, Počet zaregistrovaných voličů, Počet platných hlasů, Počet hlasů pro jednotlivé politické strany.

Nahrání potřebných knihoven:
Otevři terminál nebo příkazový řádek a spusť následující příkazy:
pip install requests
pip install beautifulsoup4
Knihovny argparse, csv a sys jsou součástí standardní knihovny Pythonu
Použití knihoven v kódu:
import requests
from bs4 import BeautifulSoup
import argparse
import csv
import sys

spuštění scriptu:
Příklad použití:
Pokud máte URL stránky volebních výsledků a chcete data uložit do souboru data.csv, spustíte skript takto:
do terminálu napíšeme:
python script_name.py "https://example.com/elections" soubor.csv
Co se děje v pozadí:
např:
python main.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103" prostejov.csv
Skript stáhne stránku ze zadané URL.
Z této stránky vyextrahuje názvy politických stran a další volební údaje.
Pro každou stranu stáhne detailní údaje (počet hlasů).
Všechna data jsou uložena v souboru prostejov.csv
URL lze měnit dle požadovaného okresku
např. pro obce v okrese Jeseník zadáme:
python main.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7101" Jesenik.csv