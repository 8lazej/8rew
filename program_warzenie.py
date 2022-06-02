from time import process_time_ns
import procesZacieranie 
import utils
import podsumowanie

BLG = 0
LITRY_PIWA = 0
LISTA_SLODOW = []

def setBLG(nowa_wartosc_BLG):
    global BLG
    BLG = nowa_wartosc_BLG

def set_litry_piwa(nowa_wartosc_litry_piwa):
    global LITRY_PIWA
    LITRY_PIWA = nowa_wartosc_litry_piwa

def nadpisz_liste_slodow(nowa_lista_slodow):
    global LISTA_SLODOW
    LISTA_SLODOW = nowa_lista_slodow

while True:
    print('Wybierz proces')
    print('[1] - Zacieranie')
    print('[2] - Chmielenie')
    print('[3] - Przeliczniki')
    print('[10] - Pokaz podsumowanie')
    wybor = input()
    if wybor == '1':
        procesZacieranie.pokaz_polecenie(setBLG, set_litry_piwa, nadpisz_liste_slodow, LITRY_PIWA)
    elif wybor == '2':
        pass
    elif wybor == '3':
        pass
    elif wybor == '10':
        podsumowanie.pokaz_podsumowanie(BLG, LITRY_PIWA, LISTA_SLODOW)
    elif wybor == utils.WYJSCIE:
        print('Milego Warzenia')
        break
    else:
        print('Błędny wpis, spróbuj jeszcze raz')
        

