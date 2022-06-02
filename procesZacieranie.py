import utils
import Slod

WYBOR_EKSTRAKT = 's'
WYBOR_WODA = 'w'

def pokaz_polecenie(setBLG, set_litry_piwa, nadpisz_liste_slodow):
    while True:
        print(f"[{WYBOR_EKSTRAKT}] - Oblicz ilość potrzebnych słodów")
        print(f"[{WYBOR_WODA}] - Oblicz ilość potrzebnej wody")
        print(utils.INTRUKCJA_WYJSCIE)
        wybor_procesu_zacierania = input()
        if wybor_procesu_zacierania == WYBOR_EKSTRAKT:
            zbierz_i_policz_ekstrakt(setBLG, set_litry_piwa, nadpisz_liste_slodow)
        elif wybor_procesu_zacierania == WYBOR_WODA:
            pass
        elif wybor_procesu_zacierania == utils.WYJSCIE:
            break



def get_float_input():
    return float(input())

def zbierz_i_policz_ekstrakt(setBLG, set_litry_piwa, nadpisz_liste_slodow):
    print('Podaj BLG')
    blg = get_float_input()
    setBLG(blg)

    print('Podaj ilość piwa w litrach')
    litry_piwa = get_float_input()
    set_litry_piwa(litry_piwa)

    print('Ekstrakt wynosi:')
    ekstrakt = policz_ekstrakt(blg, litry_piwa)
    print(ekstrakt)

    print('Podaj ilosc slodow')
    ilosc_slodow = int(input())

    nowa_lista_slodow = []
    for i in range(ilosc_slodow):
        print(f'Podaj ekstraktywnosc slodu {i+1}')
        ekstraktywnosc_slodu = get_float_input()
        
        print('Podaj procent w zasypie')
        procent_w_zasypie = get_float_input()


        kolejny_slod = Slod.Slod(ekstraktywnosc_slodu, procent_w_zasypie)
        nowa_lista_slodow.append(kolejny_slod)
    
    lista_udzialow = list(map(lambda slod: slod.procent_w_zasypie, nowa_lista_slodow))
    # print(">>>>>>>", list(lista_udzialow))
    suma_udzialow = sum(lista_udzialow)
    nadpisz_liste_slodow(nowa_lista_slodow)

    if (suma_udzialow < 99):
        raise Exception("Suma udzialow powinna byc wieksza niz 99 %")

    print('Suma rzeczywostych ekstraktow slodow wynosi:')
    suma_RES = policz_sume_rzeczyswistych_ekstraktow_slodow(nowa_lista_slodow)
    print(suma_RES)
    print('Suma zasypu w kg wynosi:')
    suma_zasypu = ekstrakt/suma_RES
    print(suma_zasypu)
    print('Slod nr x dodaj w ilosci:')
    lista_kazdego_slodu_w_kg = list(map(lambda udzial: udzial / 100 * suma_zasypu, lista_udzialow))
    # print(lista_kazdego_slodu_w_kg)
    for (index, item) in enumerate(lista_kazdego_slodu_w_kg):
        print(f'Slod #{index + 1}, {item}')


def policz_ekstrakt(BLG, litry_piwa):
    brzeczka_po_warzeniu_przed_cedzeniem = litry_piwa * 1.1
    gestosc_wlasciwa = 1 + (BLG / (258.6 - (BLG / 258.2) * 227.1))
    waga_brzeczki_po_warzeniu = brzeczka_po_warzeniu_przed_cedzeniem * gestosc_wlasciwa 
    return waga_brzeczki_po_warzeniu * BLG * 10 

def policz_sume_rzeczyswistych_ekstraktow_slodow(lista_slodow):
    suma_RESow = []
    for slod in lista_slodow:
        teoretyczny_ekstrakt_slodu_w_gramach_na_kilogram = slod.procent_ekstraktywnosci * 10
        rzeczywisty_ekstrakt_slodu_w_gramach_na_kilogram = teoretyczny_ekstrakt_slodu_w_gramach_na_kilogram * 0.75
        rzeczywisty_ekstrakt_slodu = rzeczywisty_ekstrakt_slodu_w_gramach_na_kilogram * slod.procent_w_zasypie /100
        suma_RESow.append(rzeczywisty_ekstrakt_slodu)
    return sum(suma_RESow)

