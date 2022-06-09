def pokaz_podsumowanie(parametryWarzenia):
    print("BLG: ", parametryWarzenia.getBlg())
    print('Ilosc litrow piwa: ', parametryWarzenia.getLitryPiwa())
    for (index, item) in enumerate(parametryWarzenia.getListaSlodow()):
        print(f'Slod #{index + 1}, {item}')
        print("slod xxx")
