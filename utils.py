from re import X


WYJSCIE = 'X'
INTRUKCJA_WYJSCIE = '[X] - wyjdz'
FILE_NAME = 'data.csv'
FILE_SEPARATOR = ';'
ID_COLUMN_NAME = 'ID'
NULL_DATA = 'NULL'

def get_float_input():
    while True:
        try:
            x = float(input())
            return x
        except:
            print("Podaj poprawna wartosc (moze . zamiast , ?)")
            continue