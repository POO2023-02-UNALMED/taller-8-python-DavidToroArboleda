class Deportista:
    def __init__(self, deporte, anos):
        self.deporte=deporte
        self.anos=anos

    def getDeporte(self):
        return self.deporte

    def getAñosPracticando(self):
        return self.anos

    def setDeporte(self, deporte):
        self.deporte=deporte

    def setAñosPracticando(self, anos):
        self.anos=anos
