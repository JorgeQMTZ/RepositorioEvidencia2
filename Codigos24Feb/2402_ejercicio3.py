class Producto:
    sku=""
    descripcion=0
    precio=0

    def __init__(self, sku,descripcion,precio=0):
        self.sku=sku
        self.descripcion=descripcion
        if (precio<0):
            self.precio=0
        else:
            self.precio=precio
    def MostrarProducto(self):
        print(self.sku)
        print(self.descripcion)
        print(self.precio)

class ProductoDescontinuado(Producto):
    pass

class ProductoImportado(Producto):
    pedimento=0
    paisorigen=""
    def __init__(self, sku, descripcion, pedimento, paisorigen, precio=0):
        super().__init__(sku, descripcion, precio=precio)
        self.pedimento=pedimento
        self.paisorigen=paisorigen
    def MostrarProducto(self):
        print(self.sku)
        print(self.descripcion)
        print(self.pedimento)
        print(self.paisorigen)
        print(self.precio)

obj=Producto("AP1991", "Lapiceda AKON modelo 20", -5)
 
obj.MostrarProducto()

print("...............")
prod=ProductoImportado("CC12345","Comple 1/2","AD27728","EU",-20)
prod.MostrarProducto()

class Articulo():
    idarticulo=""
    descripcion=""
    costo=0
    def __init__(self):
        self.idarticulo=""
        self.descripcion=""
        self. costo=0

miArticulo=Articulo
miArticulo.idarticulo="1010"
miArticulo.descripcion="Martillo Mod.1010"
miArticulo.costo=100
print(miArticulo.costo)
