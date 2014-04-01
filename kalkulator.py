"""Prosty kalkulator"""
import sys
log = []
def legenda():
    """Wyswietl legende"""
    print "\nDostepne operacje:\n" \
            "+ - dodawanie\n" \
            "- - odejmowanie\n" \
            "* - mnozenie\n" \
            "/ - dzielenie\n" \
            "q - zakoncz program\n" \
            "save - zapisz historie programu do pliku log.txt\n" \
            "Po wybraniu dzialania podaj liczby w nastepujacym formacie:\n" \
            "liczba liczba\n"
            
def pobierz_dzialanie():
    """Popros uzytkownika o podanie dzialania i podanie liczb"""
    dzialania = ['+', '-', '*', '/']
    while(1):
        dzialanie = raw_input("Podaj dzialanie\n")
        if dzialanie == 'q': sys.exit()
        elif dzialanie == 'save': zapisz()
        elif dzialanie in dzialania:
            return dzialanie
        else:
            print "Blad! Podaj odpowiednie dzialanie"

def pobierz_liczby():
    """Pobierz liczby"""
    liczby = 0
    while(1):
        liczby = str.split(raw_input("Podaj liczby:\n"))
        if len(liczby) != 2 :
            print "Blad! Zla ilosc liczb"
            continue
        try:
            for i in range(len(liczby)):
                liczby[i] = float(liczby[i])
            return liczby
        except ValueError:
            print "Blad! Zly format liczb"  

def zapisz():
    """Zapisz log do pliku log.txt, nadpisuje stary log"""
    plik = open('log.txt', 'w')
    for i in range(len(log)):
        plik.write(log[i] + "\n")
    plik.close()

def wykonaj():
    """Wykonaj odpowiednie dzialanie na liczbach"""
    legenda()
    while(1):
        dzialanie = pobierz_dzialanie()
        liczby = pobierz_liczby()
        wynik = {
        '+' : lambda liczby: float(liczby[0])+float(liczby[1]),
        '-' : lambda liczby: float(liczby[0])-float(liczby[1]),
        '*' : lambda liczby: float(liczby[0])*float(liczby[1]),
        '/' : lambda liczby: float(liczby[0])/float(liczby[1])
        }[dzialanie](liczby)
        print wynik
        log.append(str(liczby[0]) + " " + dzialanie + " " + str(liczby[1]) + \
                " = " + str(wynik))

wykonaj()

