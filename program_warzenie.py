import procesZacieranie 
import procesChmielenie
import procesFermentacja
import utils
from utils import get_float_input
import podsumowanie
import ParametryWarzenia


def obsluzParametryWarzenia(parametryWarzenia):
    while True:
        podaj_podstawowe_parametry(parametryWarzenia)
        print('Wybierz proces')
        print('[1] - Zacieranie')
        print('[2] - Chmielenie')
            #zmierzene parametry: temp_zacierania, RBPrzed, t1z,c1z,t2z,c2z,t3z,c3z, STYL
        print('[3] - Fermentacja')
        print('[10] - Pokaz podsumowanie')
        wybor = input()
        if wybor == '1':
            procesZacieranie.pokaz_polecenie(parametryWarzenia)
        elif wybor == '2':
            procesChmielenie.zbierz_i_policz_chmiele(parametryWarzenia)
        elif wybor == '3':
            procesFermentacja.zbierz_i_policz_alkohol(parametryWarzenia)
        elif wybor == '10':
            podsumowanie.pokaz_podsumowanie(parametryWarzenia)
        elif wybor == utils.WYJSCIE:
            print('Milego Warzenia')
            break
        else:
            print('Bledny wpis, sprobuj jeszcze raz')
        parametryWarzenia.saveToFile()
        
def podaj_podstawowe_parametry(parametryWarzenia):
    if parametryWarzenia.blg == None or parametryWarzenia.litryPiwa == None:
        print('Na początku podaj podstawowe parametry twojej warki')
        print('Podaj żądane BLG:')
        blg = get_float_input()
        print('Podaj ile litrów piwa chcesz uwarzyć:')
        litry_piwa = get_float_input()
        parametryWarzenia.blg = blg
        parametryWarzenia.litryPiwa = litry_piwa
        parametryWarzenia.saveToFile()
    
