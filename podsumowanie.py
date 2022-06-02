def pokaz_podsumowanie(BLG, LITRY_PIWA, NOWA_LISTA_SLODOW):
    print("BLG: ", BLG)
    print('Ilość litrów piwa: ', LITRY_PIWA)
    for (index, item) in enumerate(NOWA_LISTA_SLODOW):
        print(f'Slod #{index + 1}, {item}')
