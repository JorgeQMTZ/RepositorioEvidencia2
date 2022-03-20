class TablaMultiplicacion():
    NumeroBase = 0
    def GenerarTabla(self):
        for i in range(1,10):
            print(self.NumeroBase,"x",i,"=",self.NumeroBase*i)

tm = TablaMultiplicacion()
tm.NumeroBase=10

tm.GenerarTabla()

obj=TablaMultiplicacion()
obj.NumeroBase=3
obj.GenerarTabla()

tm.GenerarTabla()