from random import *

class Instrumentos:
    def afinar(self):
        pass
    
    def tocar(self):
        pass
    
    def mostrar(self):
        return "Instrumento: " + str(type(self)).split(".")[-1][:-2]

class Guitarra(Instrumentos):
    def afinar(self):
        return "Afinando guitarra"
        
    def tocar(self):
        return "Tocando guitarra"

class Saxo(Instrumentos):
    def afinar(self):
        return "Afinando saxo"
        
    def tocar(self):
        return "Tocando saxo"

class Trompeta(Instrumentos):
    def afinar(self):
        return "Afinando trompeta"
        
    def tocar(self):
        return "Tocando trompeta"

class Ukelele(Instrumentos):
    def afinar(self):
        return "Afinando ukelele"
        
    def tocar(self):
        return "Tocando ukelele"
    
class Bombo(Instrumentos):
    def afinar(self):
        return "Afinando bombo"
        
    def tocar(self):
        return "Tocando bombo"

class Flauta(Instrumentos):
    def afinar(self):
        return "Afinando flauta"
        
    def tocar(self):
        return "Tocando flauta"