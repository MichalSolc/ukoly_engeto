"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie

author: Michal Šolc
email: solc.mich@seznam.cz
"""


import requests
from bs4 import BeautifulSoup
import argparse
import csv
import sys

# Funkce pro sestavení úplné URL z relativní URL
def sestav_url(base_url: str, relative_url:str) ->str:
    """
    Tato funkce přijímá base_url (základní URL stránky) a relative_url (relativní URL).
    Sestaví a vrátí úplnou URL, kterou lze použít pro následné požadavky.
    """
    if '/' in base_url:
        return base_url[:base_url.rfind('/')] + "/" + relative_url
    return base_url

# Funkce pro získání názvů stran z dané URL
def ziskej_nazvy_stran(stranky_url: str) -> list:
    """
    vyhledá všechny buňky tabulky s určitou třídou (v tomto případě "overflow_name")
    a z těchto buněk získá text - seznam názvů politických stran.
    """
    najdi_adresu = requests.get(stranky_url) 
    if najdi_adresu.status_code == 200:
        uprav_adresu = BeautifulSoup(najdi_adresu.content, "html.parser")  
        najdi_strany = uprav_adresu.find_all("td", class_ = "overflow_name", headers = "t1sa1 t1sb2")                          
        najdi_strany2 = uprav_adresu.find_all("td", class_ = "overflow_name", headers = "t2sa1 t2sb2")
        seznam_stran = []
        for strany in najdi_strany + najdi_strany2:
            seznam_stran.append(strany.get_text().strip())
        return seznam_stran
    else:
        print("Nepodařilo se stáhnout data")
        sys.exit(1)

# Funkce pro zpracování hlavních dat z první URL
def zpracuj_data(prvni_url, soubor, strany_url):
    """
    Napíše hlavičku do CSV souboru, která obsahuje základní informace
    a názvy politických stran. Pro každý řádek tabulky
    pak stáhne podrobnosti o hlasování z druhé URL, kterou získá z odkazu
    na hlavní stránce (pomocí funkce sestav_url).
    """
    response = requests.get(prvni_url)
    if response.status_code == 200:
        
        soup = BeautifulSoup(response.content, 'html.parser')
        radky = soup.find_all('tr')
        cislo_radku = 0
        with open(soubor, 'w', encoding='utf-8') as f:
            f.write("Code;Location;Registered;Envelopes;Valid;")
            seznam_stran = ziskej_nazvy_stran(strany_url) 
            f.write(";".join(seznam_stran))
            f.write("\n")
            for radek in radky:
                bunky = radek.find_all("td")
                if len(bunky) >= 2:
                    cislo_radku += 1
                    prvni_bunka = bunky.pop(0)
                    druha_bunka = bunky.pop(0)
                    odkazy = prvni_bunka.find_all("a")
                    if odkazy:
                        prvni_odkaz = odkazy.pop(0)
                        relativni_url = prvni_odkaz.get('href')
                        druha_url = sestav_url(prvni_url, relativni_url)

                        radek_data = prvni_bunka.get_text().strip() + ";" + druha_bunka.get_text().strip()
                        seznam_stran = zpracuj_podrobnosti(druha_url, f, radek_data, cislo_radku, seznam_stran)
            if cislo_radku == 1 and seznam_stran:
                f.write(";".join(seznam_stran))
                f.write("\n")
    else:
        print("Nepodařilo se stáhnout data")

# Funkce pro zpracování podrobných dat z druhé URL
def zpracuj_podrobnosti(druha_url, soubor, radek_data, cislo_radku, seznam_stran):
    """
    Stáhne obsah podrobné stránky (druhé URL, kterou získáme z hlavní stránky).
    Extrahuje data o hlasech pro jednotlivé politické strany z tabulky na druhé URL.
    """
    response = requests.get(druha_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        radky = soup.find_all('tr')

        radek_info = ""
        seznam_hlasu = {strana: "" for strana in seznam_stran}  # Vytvoření slovníku pro uchování hlasů

        for radek in radky:
            bunky = radek.find_all("td")
            if len(bunky) == 9:
                if len(bunky) > 5:
                    prvni_bunka = bunky[3]
                    druha_bunka = bunky[4]
                    platne_hlasy_bunka = bunky[7]
                    radek_info = prvni_bunka.get_text().strip() + ";" + druha_bunka.get_text().strip() + ";" + platne_hlasy_bunka.get_text().strip()

            if len(bunky) == 5:
                if len(bunky) > 1:
                    nazev_strany = bunky[1]
                    hlasy_strany = bunky[2]  
                    nazev_strany_text = nazev_strany.get_text().strip()
                    hlasy_strany_text = hlasy_strany.get_text().strip()

                    if nazev_strany_text in seznam_hlasu:
                        seznam_hlasu[nazev_strany_text] = hlasy_strany_text

        # Zápis dat do souboru
        soubor.write(radek_data + ";" + radek_info + ";" + ";".join(seznam_hlasu.values()))
        soubor.write("\n")
        return seznam_stran
    else:
        print("Nepodařilo se stáhnout data")
        return seznam_stran

def kontrola_url(url):
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print("Chyba: URL neexistuje nebo není dostupná.")
            sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(f"Chyba: Neplatná URL nebo problém se spojením: {e}")
        sys.exit(1)

# Hlavní funkce skriptu
def hlavni(url, soubor):
    """
    hlavní funkce, která načte první URL, kde se nachází základní informace.
    Spustí proces stahování a zpracování dat.
    Zavolá funkce pro extrakci názvů politických stran a zpracování dat.
    """
    print(f"Stahuji data z URL: {url} a uložím je do souboru: {soubor}")
    pevna_strany_url = "https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=12&xobec=506761&xvyber=7103"
    zpracuj_data(url, soubor, pevna_strany_url)


if __name__ == '__main__':
    # Nastavení argumentů příkazového řádku
    parser = argparse.ArgumentParser(description='Skript pro web scraping')
    parser.add_argument('url', type=str, help='URL stránky pro stažení')
    parser.add_argument('soubor', type=str, help='Výstupní soubor')
    args =  parser.parse_args()

    # Kontrola, zda byly zadané správně oba argumenty
    if not args.soubor.endswith(".csv"):
        print("Chyba: Soubor musí mít příponu .csv")
        sys.exit(1)

    # Kontrola, zda URL nemá příponu .csv (abychom se vyhnuli záměně)
    if args.url.endswith(".csv"):
        print("Chyba: URL nemůže mít příponu .csv. Místo toho zadejte platnou URL.")
        sys.exit(1)
        
   
    
    kontrola_url(args.url)
    
    
    hlavni(args.url, args.soubor)
  