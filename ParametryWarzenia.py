from utils import FILE_NAME, FILE_SEPARATOR, ID_COLUMN_NAME, NULL_DATA

def toFloatIfExists(data):
    return float(data) if data != NULL_DATA else None

class ParametryWarzenia:
    @classmethod
    def fromRow(self, row):
        # 'ID;BLG;LITRYPIWA;RBPF'
        splitRow = row.strip().split(FILE_SEPARATOR) # [ID, BLG, ...],strip -  pozbywa sie \n np. znakow, a split dzieli po separatorze
        return ParametryWarzenia(
            splitRow[0], 
            toFloatIfExists(splitRow[1]), 
            toFloatIfExists(splitRow[2]), 
            toFloatIfExists(splitRow[3]),
            toFloatIfExists(splitRow[4]),
            toFloatIfExists(splitRow[5])
            )
    
    def __init__(
            self, 
            id, 
            blg=None, 
            litryPiwa=None, 
            rzeczywisteBLGprzedFermentacja=None, 
            BLGpoFermentacji=None, 
            ibu=None
            ):
        self.blg = blg
        self.litryPiwa = litryPiwa #definiujemy jak pola beda sie nazywaly
        self.rzeczywisteBLGprzedFermentacja = rzeczywisteBLGprzedFermentacja
        self.BLGpoFermentacji = BLGpoFermentacji
        self.id = id
        self.ibu = ibu
        

    def setBlg(self, blg):
        self.blg = blg
    def setLitryPiwa(self, litryPiwa):
        self.litryPiwa = litryPiwa
    def setListaSlodow(self, listaSlodow):
        self.listaSlodow = listaSlodow
    def setSumaZasypu(self, sumaZasypu):
        self.sumaZasypu = sumaZasypu
    def setSumaIBU(self, SumaIBU):
        self.SumaIBU = SumaIBU
    def getBlg(self):
        return self.blg
    def getLitryPiwa(self):
        return self.litryPiwa
    # def nazwana_funkcja():
    #   return self.item
    #
    # lambda: self.item
    #
    # def nazwana_funkcja_2(x, y):
    #   return x + y
    #
    # lambda x,y: x+y
    def getListaSlodow(self):
        return self.tryGetValue(lambda: self.listaSlodow, [])
    def getSumaZasypu(self):
        return self.tryGetValue(lambda: self.sumaZasypu, None)
        

    def convertParametryWarzeniaToRow(self):
        listOfProperties = [self.id, self.blg, self.litryPiwa, self.rzeczywisteBLGprzedFermentacja, self.BLGpoFermentacji, self.ibu]
        listOfPropsWithEmptySpaceInsteadOfNone = map(lambda prop: NULL_DATA if prop is None else prop, listOfProperties)
        return ';'.join(map(lambda prop: str(prop), listOfPropsWithEmptySpaceInsteadOfNone)) + '\n'

    def getListOfHeaders(self):
        return [ID_COLUMN_NAME, 'BLG','Litry_piwa','BLGprzedFermentacja', 'BLGpoFermentacji', 'IBU']
        
    def saveToFile(self):
        hasBeenUpdated = False
        with open(FILE_NAME, 'r') as file:
            lines = file.readlines()
            # for x in lines:
            #     print(x)
            # print('tu linie',lines)
        with open(FILE_NAME, 'w') as file:
            if lines == []:
                file.write(FILE_SEPARATOR.join(self.getListOfHeaders()) + '\n')
            for line in lines:
                if (line.split(FILE_SEPARATOR)[0] == self.id):
                    file.write(self.convertParametryWarzeniaToRow())
                    hasBeenUpdated = True
                    print('wszedlem',self.id, line.split(FILE_SEPARATOR)[0])
                else:
                    print('>>>>',line)
                    file.write(line)
            
            if not hasBeenUpdated:
                file.write(self.convertParametryWarzeniaToRow())

    def tryGetValue(self, getValueAction, default):
        try:
            x = getValueAction()
            return x
        except:
            print("Ta wartosc nie zostaly nigdy zapisana do pliku")
            return default


    
    
    