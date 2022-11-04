from Animal import Animal

class Bovino(Animal):
    def __init__(self):
        self.propietario=""
        self.fecha_vacunacion=""
        self.establo=int
        
    def pastar(self):
        if self.establo<=5:
            print("No pastar")
        else:
            print("Pastar")
    
    def emitir_sonido(self):
        print("Muuu")