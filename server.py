import clase
import Pyro4
Bodega=clase.Almacen()
v1=clase.Visitante('Edgar',22)
v2=clase.Visitante('Jean',21)

daemon = Pyro4.Daemon()
uri = daemon.register(Bodega)
uriv1 = daemon.register(v1)
uriv2 = daemon.register(v2)
print(uri)
print(uriv1)
print(uriv2)
daemon.requestLoop()