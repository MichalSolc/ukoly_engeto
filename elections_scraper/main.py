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
    if '/' in base_url:
        return base_url[:base_url.rfind('/')] + "/" + relative_url
    return base_url

# Funkce pro získání názvů stran z dané URL
def ziskej_nazvy_stran(stranky_url: str) -> list:
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

# Funkce pro získání dat o hlasech pro jednotlivé strany
def ziskej_hlasy_z_radku(radek, seznam_hlasu):
    bunky = radek.find_all("td")
    if len(bunky) == 5:
        if len(bunky) > 1:
            nazev_strany = bunky[1]
            hlasy_strany = bunky[2]  
            nazev_strany_text = nazev_strany.get_text().strip()
            hlasy_strany_text = hlasy_strany.get_text().strip()

            if nazev_strany_text in seznam_hlasu:
                seznam_hlasu[nazev_strany_text] = hlasy_strany_text
    return seznam_hlasu

# Funkce pro extrakci hlavních volebních dat z druhé URL
def zpracuj_podrobnosti(druha_url, soubor, radek_data, cislo_radku, seznam_stran):
    """
    Funkce provede požadavek na druhou URL a analyzuje HTML obsah. 
    Extrahuje data o hlasech pro politické strany pomocí funkce ziskej_hlasy_z_radku
    a základní volební informace pomocí funkce extrahuj_radek_info. 
    Výsledné hodnoty zapíše do CSV souboru.
    """
    response = requests.get(druha_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        radky = soup.find_all('tr')

        radek_info = ""
        seznam_hlasu = {strana: "" for strana in seznam_stran}

        for radek in radky:
            bunky = radek.find_all("td")
            if len(bunky) == 9:
                radek_info = extrahuj_radek_info(bunky)

            seznam_hlasu = ziskej_hlasy_z_radku(radek, seznam_hlasu)

        soubor.write(radek_data + ";" + radek_info + ";" + ";".join(seznam_hlasu.values()))
        soubor.write("\n")
        return seznam_stran
    else:
        print("Nepodařilo se stáhnout data")
        return seznam_stran

# Funkce pro extrakci hlavních volebních dat (voliči v seznamu, vydané obálky, platné hlasy) z buněk
def extrahuj_radek_info(bunky):
    prvni_bunka = bunky[3]
    druha_bunka = bunky[4]
    platne_hlasy_bunka = bunky[7]
    return prvni_bunka.get_text().strip() + ";" + druha_bunka.get_text().strip() + ";" + platne_hlasy_bunka.get_text().strip()

# Funkce pro zápis dat do CSV souboru
def zapis_do_souboru(soubor, seznam_stran, radky, prvni_url, strany_url):
    """
    Funkce prochází všechny řádky tabulky na první stránce,
    extrahuje potřebná data (např. název obvodu, počet registrovaných voličů)
    a pro každý řádek volá funkci zpracuj_podrobnosti pro získání
    detailních informací o hlasování. Všechny tyto informace se následně 
    zapisují do souboru.
    """
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

# Stáhne data z první URL a předá je k dalšímu zpracování.
def zpracuj_data(prvni_url, soubor, strany_url):
    response = requests.get(prvni_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        radky = soup.find_all('tr')
        zapis_do_souboru(soubor, [], radky, prvni_url, strany_url)
    else:
        print("Nepodařilo se stáhnout data")

# Ověří, zda je zadaná URL platná 
def kontrola_url(url):
    """
    pokud je URL platná, pokračuje skript; pokud není, skript se ukončí.
    """
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print("Chyba: URL neexistuje nebo není dostupná.")
            sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(f"Chyba: Neplatná URL nebo problém se spojením: {e}")
        sys.exit(1)

# Hlavní funkce skriptu, která řídí celý proces stahování a zpracování dat.
def hlavni(url, soubor):
    """
    Funkce zavolá všechny potřebné funkce k získání volebních dat a jejich zápisu do CSV souboru.
    Nejdříve se zavolá funkce zpracuj_data, která začne celý proces stahování dat.
    """

    print(f"Stahuji data z URL: {url} a uložím je do souboru: {soubor}")
    pevna_strany_url = "https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=12&xobec=506761&xvyber=7103"
    zpracuj_data(url, soubor, pevna_strany_url)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Skript pro web scraping')
    parser.add_argument('url', type=str, help='URL stránky pro stažení')
    parser.add_argument('soubor', type=str, help='Výstupní soubor')
    args =   parser.parse_args()

    if not args.soubor.endswith(".csv"):
        print("Chyba: Soubor musí mít příponu .csv")
        sys.exit(1)

    if args.url.endswith(".csv"):
        print("Chyba: URL nemůže mít příponu .csv. Místo toho zadejte platnou URL.")
        sys.exit(1)

    kontrola_url(args.url)
    hlavni(args.url, args.soubor)