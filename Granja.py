from Animal import Animal
from Perro import Perro
from Bovino import Bovino

class Granja:
    def __init__(self,Animal,Perro,Bovino):
        self.perros=[2]
        self.bovinos=[3]
        self.mis_perros=Perro
        self.mis_bovinos=Bovino
    
    def agregar_perro(self,peso,edad,raza,fecha_vacunacion,propietario):
        perro=Perro()
        perro.peso=peso
        perro.edad=edad
        perro.raza=raza
        perro.fecha_vacunacion=fecha_vacunacion
        perro.propietario=propietario
    
    def agregar_bovino(self,peso,edad,raza,fecha_vacunacion,propietario,establo):
        bovino=Bovino()
        bovino.peso=peso
        bovino.edad=edad
        bovino.raza=raza
        bovino.fecha_vacunacion=fecha_vacunacion
        bovino.propietario=propietario
        bovino.establo=establo
    
    def obtener_perro(self,indice):
        return self.mis_perros[indice]
    
    def obtener_bovino(self,indice):
        return self.mis_bovinos[indice]
    