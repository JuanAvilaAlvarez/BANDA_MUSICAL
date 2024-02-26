from random import *

class Instrumento:
    def __init__(self, intrumento):
        self.intrumento = intrumento
    
    def asignar(self):
        self.intrumento = random.choice("Piano", "Guitarra")