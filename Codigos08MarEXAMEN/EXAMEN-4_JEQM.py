#Pregunta4

def relacion(a, b):
    if a > b: 
        return 1
    elif a < b:
        return -1
    else:
        return 0

print( relacion(20, 30) )
print( relacion(30, 15) )
print( relacion(35, 35) )