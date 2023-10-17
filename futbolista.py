from persona import Persona
from deportista import Deportista

class Futbolista(Persona, Deportista):
    def __init__(self, name, edad, altura, sexo, anos, goles, tRojas, pierna):
        Persona.__init__(self, name, edad, altura, sexo)
        Deportista.__init__(self, "Futbol", anos)
        self.goles=goles
        self.tRojas=tRojas
        self.pierna=pierna

    def getGolesMarcados(self):
        return self.goles

    def getTarjetasRojas(self):
        return self.tRojas

    def getPiernaHabil(self):
        return self.pierna

    def setGolesMarcados(self, goles):
        self.goles=goles

    def setTarjetasRojas(self, tRojas):
        self.tRojas=tRojas

    def setPiernaHabil(self, pierna):
        self.pierna=pierna

    def __str__(self):
        return "Mi nombre es " + self.getNombre() + " soy profesional en el deporte " + self.getDeporte() + " Tengo " + str(self.getEdad()) + " años de edad y llevo " + str(self.getAñosPracticando()) + " años en el deporte"
