class saludo:
    def saludar(self, nombre):
        print('Hola', nombre)
        
nombre = input("Introduce tu nombre: ")
s = saludo()
s.saludar(nombre)