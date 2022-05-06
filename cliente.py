import Pyro4
b=Pyro4.Proxy("PYRO:bolsa@localhost:9090")
def pedirNumeroEntero():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce una opcion: "))
            correcto=True
        except ValueError:
            print('Error, introduce una opcion valida')
     
    return num

salir = False
opcion = 0

while not salir:
    print ("===================================================================")
    print("===========================ALMACEN==================================")
    print ("===================================================================")   
    print ("1.-REGISTRAR EN EL AMLACEN")
    print ("2.-ELIMINAR DEL AMLACEN")
    print ("3.-INVENTARIO")
    print ("4.-VISITANTES")
    print ("5.-SALIR")
    print ("===================================================================")
    print ("ELIGE UNA OPCION")
 
    opcion = pedirNumeroEntero()
 
    if opcion == 1:
        nom=input('Ingrese el nombre del producto:')
        cod=input('Ingrese el codigo:')
        vist=input('Ingrese el nombre del visitante:')
        b.ingresarArt(nom,cod,vist)
    elif opcion == 2:
        cod=input('Ingrese el codigo:')
        vist=input('Ingrese el nombre del visitante:')
        b.eliminarArt(cod,vist)
    elif opcion == 3:
        b.inventario()
    elif opcion == 4:
        b.historialVisit()
    elif opcion == 5:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 3")
 
print ("Fin")
    