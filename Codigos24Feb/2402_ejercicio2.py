import datetime

class Pais:
    def __init__(self,NombreIng,NombreEsp,Fallecidos, Contagiados, PDC):
        self.NombreIng = NombreIng
        self.NombreEsp = NombreEsp
        self.Fallecidos = Fallecidos
        self.Contagiados = Contagiados
        self.PDC = PDC

class Incidente:
    def __init__(self,Pais2,Fecha,NContangios,NFallecidos):
        self.Fecha = Fecha
        self.Pais2 = Pais2
        self.NContangios = NContangios
        self.NFallecidos = NFallecidos

miPais = Pais(str("Mexico"),str("Mexico"),int(1000),int(5000),datetime.datetime(2020,5,18))
print(miPais.PDC)

incidenteAyer = Incidente(datetime.datetime(2020, 5, 17),str("Mexico"),int(1500),int(18))
incidenteHoy = Incidente(datetime.datetime.now(),str("Mexico"),int(1400),int(12))
print(incidenteAyer.Pais2)