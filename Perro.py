from Animal import Animal

class Perro(Animal):
    def __init__(self):
        self.propietario=""
        self.fecha_vacunacion=""
        
    def emitir_sonido(self):
        if self.edad>=3:
            print("Guau Guau")
        else:
            print("Auf Auf")
