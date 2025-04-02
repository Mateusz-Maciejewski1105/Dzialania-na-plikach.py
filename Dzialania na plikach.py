import random
import os

opcja = 't'  
while opcja == 't':  
    print("********************ZAPIS DANYCH DO PLIKÓW********************")  
    print("1 - Opcja 1")  
    print("2 - Opcja 2")  
    print("0 - Koniec")  

    try:  
        wybor = int(input("Wybierz jedną z opcji:\n"))  
    except ValueError:  
        print("Błąd! Wprowadź poprawną liczbę całkowitą.")  
        continue  

    if wybor == 1:  
        plik = open('plik.txt', 'w')  
        liczby = []  
        for i in range(6):  
            while True:  
                try:  
                    a = int(input(f"Podaj {i + 1} liczbę (1-49): "))  
                    if 1 <= a <= 49:  
                        if a not in liczby:  # Sprawdzenie, czy liczba jest unikalna  
                            liczby.append(a)  
                            break  
                        else:  
                            print("Liczba już została podana! Podaj inną liczbę.")  
                    else:  
                        print("Liczba musi być z zakresu 0-49! Spróbuj ponownie!")  
                except ValueError:  
                    print("Błąd! Wprowadź poprawną liczbę całkowitą.")  

        losowe = []  
        for i in range(6):  
            b = random.randint(1, 49)  
            losowe.append(b)  

        if set(liczby) & set(losowe):  
            trafione = list(set(liczby) & set(losowe))  
            print(f"Trafiłeś następujące liczby: {trafione}")  
            print(f"Liczba trafień: {len(trafione)}")  
            print(f"Wprowadzone liczby to: {liczby}")  
            print(f"Wylosowane liczby to: {losowe}")  
            plik.write("Losowanie przebiegło pomyślnie\n")  
            plik.write(f"Wprowadzone liczby to: {liczby}\n")  
            plik.write(f"Wylosowane liczby to: {losowe}\n")  
            plik.write(f"Liczba trafień: {len(trafione)}\n")  
            plik.write(f"Trafiłeś następujące liczby: {trafione}")  
        else:  
            print("Niestety nie trafiłeś żadnej liczby")
            print(f"Wprowadzone liczby to: {liczby}")
            print(f"Wylosowane liczby to: {losowe}")
            plik.write("Losowanie przebiegło pomyślnie\n")  
            plik.write(f"Wprowadzone liczby to: {liczby}\n")  
            plik.write(f"Wylosowane liczby to: {losowe}\n")  
            plik.write("Nie trafiłeś żadnej liczby")  
        plik.close()
    
        
    elif(wybor==2):  
        if not os.path.exists('oswiadczyny.txt'):  
            print("Plik 'oswiadczyny.txt' nie istnieje! Upewnij się, że plik znajduje się w katalogu programu.")  
        else:  
            plikO = open('oswiadczyny.txt', 'r', encoding='utf-8')  
            plikZapis = open('Zapis.txt', 'w', encoding='utf-8')  
            zawartosc = plikO.read()  
            szukana = input("Podaj znak lub ciąg znaków, który szukasz")  
            liczbaWystapien = zawartosc.count(szukana)  
            print(f"Liczba wystąpień '{szukana}': {liczbaWystapien}")  
            indeks = zawartosc.find(szukana)  
            if indeks != -1:  
                print(f"Pierwsze wystąpienie '{szukana}' znajduje się na pozycji: {indeks}")  
                plikZapis.write(f"Poszukiwany znak/łańcuch to {szukana} i w pliku oswiadczyny.txt został znaleziony {liczbaWystapien}")  
            else:  
                print(f"Nie znaleziono '{szukana}' w pliku.")  
                plikZapis.write(f"Poszukiwany znak/łańcuch to {szukana} ale nie został znaleziony ani razu")  
            print("ODWROCONY TEKST")  
            odwroconyTekst = zawartosc[::-1]  
            print(odwroconyTekst)  
            print("POŁOWA DRUKOWANEGO TEKSTU")  
            TekstDrukowany = ''.join(char.upper() if i % 2 == 0 else char for i, char in enumerate(zawartosc))  
            print(TekstDrukowany)  
        
           
            plikO.close()
            plikZapis.close()
        
    elif(wybor==0):
        print("Koniec programu. Do widzenia!")
        exit()
    else:
        print("Wybrałeś niepoprawnie spróbuj ponownie!")
    opcja = input("Czy chcesz kontunuować? (t/n): ").lower()
    if opcja != 't':
        break
