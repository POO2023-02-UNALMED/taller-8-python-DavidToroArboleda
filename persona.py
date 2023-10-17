class Persona:
    def __init__(self, name, edad, altura, sexo):
        self.nombre=name
        self.edad=edad
        self.altura=altura
        self.sexo=sexo

    def getNombre(self):
        return self.nombre

    def getEdad(self):
        return self.edad

    def getAltura(self):
        return self.altura

    def getSexo(self):
        return self.sexo

    def setNombre(self, name):
        self.nombre=name

    def setEdad(self, edad):
        self.edad=edad

    def setAltura(self, altura):
        self.altura=altura

    def setSexo(self, sexo):
        self.sexo=sexo

