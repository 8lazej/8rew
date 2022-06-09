import PercentageException 

class Chmiel:
    def __init__(self, masa_chmielu, alfakwasy, wykorzystanie):
        self.masa_chmielu = masa_chmielu
        self.alfakwasy = alfakwasy
        self.wykorzystanie = wykorzystanie
    def __str__(self):
        return f" masa chmielu: {self.masa_chmielu}, alfakwasy: {self.alfakwasy}, wykorzystanie: {self.wykorzystanie} "

