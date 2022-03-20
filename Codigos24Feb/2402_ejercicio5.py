import datetime
import re

class Producto:
    def __init__(self, Codigo, Descripcion="", PrecioUnitario=0.00):
        self.Codigo=Codigo
        self.Descripcion=Descripcion
        self.PrecioUnitario=PrecioUnitario

class ProductoImportado(Producto):
    def __init__(self, Codigo, Descripcion, PrecioUnitario, FechaImportacion=datetime.datetime.now(),NumeroPedimento="",EsValido=False):
        super().__init__(Codigo, Descripcion, PrecioUnitario)
        self.FechaImportacion=FechaImportacion
        self.NumeroPedimento=NumeroPedimento
        self.EsValido=EsValido

    def Validar(self):
        if re.search(r"[0-9]{6}",self.Codigo):
            self.EsValido=True
        else:
            self.EsValido=False
            
x=ProductoImportado("123","Primer Producto",100.00) 
x.NumeroPedimento="1234567890"
x.Validar()

print(x.Codigo)
print(x.PrecioUnitario)
print(x.NumeroPedimento)
print(x.EsValido)
