

from utils import get_float_input


def zbierz_i_policz_alkohol(parametryWarzenia):
    print('Podaj zmierzony ekstrakt po fermentacji')
    ekstraktPOfermentacja = get_float_input()
    parametryWarzenia.BLGpoFermentacji = ekstraktPOfermentacja
    ekstraktPRZEDfermentacja = parametryWarzenia.rzeczywisteBLGprzedFermentacja
    procent_alkoholu = (ekstraktPRZEDfermentacja - ekstraktPOfermentacja)/1.9
    print(f'Orientacyjny poziom alkoholu wynosi {procent_alkoholu}%')