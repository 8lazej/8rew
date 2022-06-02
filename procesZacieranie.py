import utils
import Slod

WYBOR_EKSTRAKT = 's'
WYBOR_WODA = 'w'

def pokaz_polecenie(setBLG, set_litry_piwa, nadpisz_liste_slodow, litry_piwa):
    lista_sumy_slodow = []

    while True:
        print(f"[{WYBOR_EKSTRAKT}] - Oblicz ilość potrzebnych słodów")
        print(f"[{WYBOR_WODA}] - Oblicz ilość potrzebnej wody")
        print(utils.INTRUKCJA_WYJSCIE)
        wybor_procesu_zacierania = input()
        if wybor_procesu_zacierania == WYBOR_EKSTRAKT:
            zbierz_i_policz_ekstrakt(setBLG, set_litry_piwa, nadpisz_liste_slodow, lista_sumy_slodow)
        elif wybor_procesu_zacierania == WYBOR_WODA:
            zbierz_i_policz_wode(setBLG, set_litry_piwa, lista_sumy_slodow, litry_piwa)
        elif wybor_procesu_zacierania == utils.WYJSCIE:
            break



def get_float_input():
    return float(input())

def zbierz_i_policz_ekstrakt(setBLG, set_litry_piwa, nadpisz_liste_slodow, lista_slodow):
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

    for slod_w_kg in lista_kazdego_slodu_w_kg:
        lista_slodow.append(slod_w_kg)

    # print(lista_kazdego_slodu_w_kg)
    for (index, item) in enumerate(lista_kazdego_slodu_w_kg):
        print(f'Slod #{index + 1}, {item}')

def zbierz_i_policz_wode(setBLG, set_litry_piwa, lista_sumy_slodow, litry_piwa):
    print('Podaj wspolczynnik 1 kg slodu do x l wody')
    wspolczynnik_slod_woda = get_float_input()
    print('Woda potrzebna do zacierania w litrach:')
    suma_listy_slodow = sum(lista_sumy_slodow)
    woda_do_zacierania = suma_listy_slodow * wspolczynnik_slod_woda
    print(woda_do_zacierania)
    print('Woda potrzebna do wysładzania w litrach')
    woda_do_wysladzania = policz_sume_wody_do_wysladzania(litry_piwa, suma_listy_slodow, woda_do_zacierania)
    print(woda_do_wysladzania)



    print(sum(lista_sumy_slodow))

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

def policz_sume_wody_do_wysladzania(litryPiwa, suma_listy_slodow, woda_do_zacierania):
    print('>>>>>>')
    woda_pozotala_w_mlocie = suma_listy_slodow
    woda_odparowana_przy_chmieleniu = litryPiwa * 0.15
    straty_chmiel_gestwa = litryPiwa * 0.1
    woda_do_uzupelnienia = litryPiwa - woda_do_zacierania
    print(woda_pozotala_w_mlocie, woda_odparowana_przy_chmieleniu, straty_chmiel_gestwa, woda_do_uzupelnienia, sep="----")
    # return woda_pozotala_w_mlocie + woda_odparowana_przy_chmieleniu + straty_chmiel_gestwa + woda_do_uzupelnienia