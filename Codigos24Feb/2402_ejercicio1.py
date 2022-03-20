class GestionNumerica():
    Operador1 = 0
    Operador2 = 0
    
    def sumar(self):
        return self.Operador1 + self.Operador2

    def multiplicar(self):
        return self.Operador1 * self.Operador2

    def restar(self):
        return self.Operador1 - self.Operador2

    def dividir(self):
        return self.Operador1 / self.Operador2

mi_objeto = GestionNumerica()
mi_objeto.Operador1 = 10
mi_objeto.Operador2 = 5

print(mi_objeto.Operador1)
print(mi_objeto.Operador2)
print(mi_objeto.sumar())
print(mi_objeto.multiplicar())
print(mi_objeto.restar())
print(mi_objeto.dividir())
