import Pyro4

class Objeto:
    def __init__(self,nombre,codigo,estado):
        self.nombre=nombre
        self.codigo=codigo
        self.estado=estado

class Visitante:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
        self.motivo=''

@Pyro4.expose
class Almacen:
    listaArt=[]
    listaVist=[]
    def ingresarArt(self,nombre,codigo,visit):
        motivo='Ingreso de art.'
        #self.listaVist.append(visit)
        estado='Almacenano por: '+visit
        self.listaArt.append(Objeto(nombre,codigo,estado))
        print('Articulo almacenado por:',visit)
    def eliminarArt(self,codigo,visit):
        visit.motivo='Retiro de art.'
        self.listaVist.append(visit)
        for i in self.listaArt:
            if(i.codigo==codigo):
                self.listaArt.remove(i)
                print('Articulo ',i.nombre,' retirado por:',visit.nombre)
    def inventario(self):
        print('Total:',len(self.listaArt))
        if(len(self.listaArt)==0):
            print('Almacen Vacio')
        else:
            print('Articulos:')
            print('Nombre','\tCodigo','\tEstado')
            for i in self.listaArt:
                print(i.nombre, end =" "),print('\t',i.codigo, end =" "),print('\t',i.estado)
    def historialVisit(self):
        print('Nombre','\tEdad','\tMotivo')
        for i in self.listaVist:
            print(i.nombre, end =" "),print('\t',i.edad, end =" "),print('\t',i.motivo)


