#Pregunta5

def validar(correo):
    caracterBuscado="@"
    correovalido=False
    for c in correo:
        if c==caracterBuscado:
            return True
    return False

 
correo=input("Dime tu correo: ")
if validar(correo):
    print("Correo valido")
else:
    print("Correo no valido")