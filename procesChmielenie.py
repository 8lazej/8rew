
import utils
import Chmiel

from procesZacieranie import get_float_input


def zbierz_i_policz_chmiele(parametryWarzenia):
    print('Podaj ilosc chmieli')
    ilosc_chmieli = int(input())

    nowa_lista_chmieli = []
    for i in range(ilosc_chmieli):
        print('Podaj mase w gramach chmielu' + str(i+1))
        masa_chmielu = get_float_input()
        
        print('Podaj procent alfa kwasów chmielu'+ str(i+1))
        alfakwasy = get_float_input()

        print('Podajsz czas w min. gotowania chmielu' + str(i+1))
        #to trzeba zamienic na wykorzystanie
        czas = get_float_input()
        wykorzystanie = oblicz_wykorzystanie(czas)

        kolejny_chmiel = Chmiel.Chmiel(masa_chmielu, alfakwasy, wykorzystanie)
        nowa_lista_chmieli.append(kolejny_chmiel)
        
    parametryWarzenia.chmiele = nowa_lista_chmieli
    ibu = obliczIBU(nowa_lista_chmieli, parametryWarzenia)
    print('IBU wynosi:')
    print(ibu)
    print('Po chmieleniu zmierz rzeczywiste BLG przed fermentacją i je podaj:')
    rzeczywiste_blg_przed_fermentacja = get_float_input()
    parametryWarzenia.rzeczywisteBLGprzedFermentacja = rzeczywiste_blg_przed_fermentacja
    parametryWarzenia.ibu = ibu


def oblicz_wykorzystanie(czas):
    MAKSYMALNE_WYKORZYSTANIE = 34
    table = [
        [9, 6],
        [19, 15],
        [29, 19],
        [44, 24],
        [59, 27],
        [74, 30],
    ]

    for [czas_gotowania, wykorzystanie] in table:
        if (czas < czas_gotowania):
            return wykorzystanie
    return MAKSYMALNE_WYKORZYSTANIE

    

def obliczIBU(lista_chmieli, parametryWarzenia):
    lista_IBU = []
    litryPiwa = parametryWarzenia.litryPiwa

    for chmiel in lista_chmieli:
        IBUslodu = (chmiel.masa_chmielu * chmiel.alfakwasy * chmiel.wykorzystanie)/(litryPiwa * 10)
        lista_IBU.append(IBUslodu)
    return sum(lista_IBU)