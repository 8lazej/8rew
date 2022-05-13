import utils

WYBOR_EKSTRAKT = 'e'
WYBOR_WODA = 'w'

def pokaz_polecenie():
    while True:
        print(f"[{WYBOR_EKSTRAKT}] - ekstrakt")
        print(f"[{WYBOR_WODA}] - woda")
        print(utils.INTRUKCJA_WYJSCIE)
        wybor_procesu_zacierania = input()
        if wybor_procesu_zacierania == WYBOR_EKSTRAKT:
            zbierz_i_policz_ekstrakt()
        elif wybor_procesu_zacierania == WYBOR_WODA:
            pass
        elif wybor_procesu_zacierania == utils.WYJSCIE:
            break


def policz_ekstrakt(x, y, z):
    return x + y - z

def get_float_input():
    return float(input())

def zbierz_i_policz_ekstrakt():
    print('podaj x')
    x = get_float_input()
    print('podaj y')
    y = get_float_input()
    print('podaj z')
    z = get_float_input()
    print('Ekstrakt wynosi:')
    print(policz_ekstrakt(x, y, z))