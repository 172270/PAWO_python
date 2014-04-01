"""Mastermind game"""
import random
def losuj():
    """Wylosuj 4 cyfry"""
    lista = []
    for _ in range(4):
        lista.append(random.choice(range(10)))
    return lista

def pobierz():
    """Popros uzytkownika o 4 cyfry i sprawdz ich poprawnosc"""
    zgadnij = []
    i = 0
    while(i<4):
        try:
            cyfra = int(raw_input("Podaj cyfre\n"))
            if cyfra in range(10):
                zgadnij.append(cyfra)
                i += 1
            else:
                print "Blad! Podaj cyfre"
        except ValueError:
            print "Blad! Podaj cyfre"
    return zgadnij

def sprawdz(lista, zgadnij):
    """Sprawdz ile cyfr uzytkownik odgadl"""
    wynik = []
    for i in range(4):
        if zgadnij[i] in lista:
            if lista[i] == zgadnij[i]:
                wynik.append(2)
            else:       
                wynik.append(1)
    random.shuffle(wynik)
    print wynik
    if lista == zgadnij:
        return 0
    else:
        return 1

def main():
    """Main function"""
    print "\n\nLEGENDA\n" \
            "1 - cyfra trafiona ale w zlym miejscu\n" \
            "2 - cyfra trafiona i w dobrym miejscu\n" \
            "kolejnosc cyfer w podpowiedzi jest losowa"
    lista = losuj()
    runda = 1
    while (sprawdz(lista, pobierz()) and runda < 10):
        runda += 1
    if runda >= 10:
        print "Niestety przekroczyles limit 10 rund\n" \
            "Prawidlowa odpowiedz to: "
        print lista
    else:
        print "Brawo, wygrales!"

main()

# jakie sa zalety wykorzystania konstrukcji ponizej 
# skoro mozna po prostu wywolac funkcje tak jak wyzej ?

#if __name__ == '__main__':
#    main()
