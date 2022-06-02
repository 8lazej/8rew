import PercentageException 

class Slod:
    def __init__(self, procent_ekstraktywnosci, procent_w_zasypie):
        if procent_ekstraktywnosci < 0 or procent_ekstraktywnosci > 100:
            raise PercentageException
        if procent_w_zasypie < 0 or procent_w_zasypie > 100:
            raise PercentageException
        self.procent_ekstraktywnosci = procent_ekstraktywnosci
        self.procent_w_zasypie = procent_w_zasypie

    def __str__(self):
        return "{procent ekstraktywnosci " + str(self.procent_ekstraktywnosci) + " procent slodu w zasypie " + str(self.procent_w_zasypie) + "}"

    
