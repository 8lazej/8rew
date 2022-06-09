import ParametryWarzenia
import program_warzenie
from utils import FILE_NAME, FILE_SEPARATOR, ID_COLUMN_NAME

print('Witaj w 8rew!\n \
    Jest to program wspomagający zarządzanie procesami biochemicznymi w procesie produkcji piwa domowego\n \
    Aby poruszać się po programie, w konsoli terminala wpisz znak znajdujący się w nawiasie kwadratowym [] \n \
    po czym wciśnij enter\n \
    Na przykład jeśli chcesz utworzyć nową warkę, wybierz 1 i zatwierdź' )
def utworzNowaWarke():
    print('Podaj ID nowej warki')
    idNowejWarki = input()
    parametryWarzenia = ParametryWarzenia.ParametryWarzenia(idNowejWarki)
    program_warzenie.obsluzParametryWarzenia(parametryWarzenia)

def edytujObecnaWarke():
    print('Podaj ID warki')
    idWarki = input()
    #
    # [row for row in file if 'ID' in row]
    # ===
    # rows = []
    # for row in file:
    #   if 'ID' in row:
    #       rows.append(row)
    #
    with open(FILE_NAME, 'r') as file:
        rows = [row for row in file if ID_COLUMN_NAME not in row] # ['1;15;15', '2;15;89', '3;90;78']
        filtered_rows = list(filter(lambda row: row.split(FILE_SEPARATOR)[0] == idWarki, rows))
        if len(filtered_rows) == 1:
            parametryWarzenia = ParametryWarzenia.ParametryWarzenia.fromRow(filtered_rows[0])
            program_warzenie.obsluzParametryWarzenia(parametryWarzenia)
        else:
            raise Exception("nie istnieje taka warka lub blad w pliku")

while True:
    print("Wybierz")
    print("[1] - utwórz nową warkę")
    print("[2] - edytuj obecną warke")

    wybor = input()
    if (wybor == '1'):
        utworzNowaWarke()
    elif (wybor == '2'):
        edytujObecnaWarke()
    else:
        raise Exception('Błędnie wpisana wartość')

    
