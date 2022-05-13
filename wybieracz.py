from time import process_time_ns
import procesZacieranie 
import utils

while True:
    print('Wybierz proces')
    print('[1] - aijsdaljsida')
    print('[2] - aaaaaaaaaaaaaaaaa')
    print('[3] - appoqwpowqpowqopqw')
    wybor = input()
    if wybor == '1':
        procesZacieranie.pokaz_polecenie()
    elif wybor == '2':
        pass
    elif wybor == '3':
        pass
    elif wybor == utils.WYJSCIE:
        print('Milego Warzenia')
        break
    else:
        print('Błędny wpis, spróbuj jeszcze raz')
        

