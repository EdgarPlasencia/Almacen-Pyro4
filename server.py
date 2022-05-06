
import clase
import Pyro4

Almacen=clase.Almacen()

Pyro4.Daemon.serveSimple({
    Almacen: 'bolsa',
}, host="localhost", port=9090, ns=False, verbose=True)