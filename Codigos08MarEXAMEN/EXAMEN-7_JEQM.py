#Pregunta7

positivo=0
numero=int(input("Ingrese un numero: "))
while numero!=0:
    if numero>0:
        positivo+=1
    numero=int(input("Ingrese un numero: "))
    
print("Cantidad de numeros positivos ingresados:")
print(positivo)