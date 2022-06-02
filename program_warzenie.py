from time import process_time_ns
import procesZacieranie 
import utils
import podsumowanie
import ParametryWarzenia

parametryWarzenia = ParametryWarzenia.ParametryWarzenia()

while True:
    print('Wybierz proces')
    print('[1] - Zacieranie')
    print('[2] - Chmielenie')
    print('[3] - Przeliczniki')
    print('[10] - Pokaz podsumowanie')
    wybor = input()
    if wybor == '1':
        procesZacieranie.pokaz_polecenie(parametryWarzenia)
    elif wybor == '2':
        pass
    elif wybor == '3':
        pass
    elif wybor == '10':
        podsumowanie.pokaz_podsumowanie(parametryWarzenia)
    elif wybor == utils.WYJSCIE:
        print('Milego Warzenia')
        break
    else:
        print('Błędny wpis, spróbuj jeszcze raz')
        

