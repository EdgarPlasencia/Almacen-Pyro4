import Pyro4
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

uri="PYRO:obj_81b638d06ced43c9829cd89831ef18d3@localhost:37191"
llamada=Pyro4.Proxy(uri)
llamada.inventario()
print ("===================================================================")
print("================== Almacenes tu vieja ==============================")
print ("===================================================================")
print ("1.-REGISTRAR EN EL AMLACEN")
print ("2.-ELIMINAR DEL AMLACEN")
print ("3.-INVENTARIO")
print ("4.-VISITANTES")
print ("5.-SALIR")
print ("===================================================================")
print ("===================def pedirNumeroEntero():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
     
    return num
    print ("3. Opcion 3")
    print ("4. Salir")
     
    print ("Elige una opcion")
 
    opcion = opcionsele()
 
    if opcion == 1:
        print ("Opcion 1")
    elif opcion == 2:
        print ("Opcion 2")
    elif opcion == 3:
        print("Opcion 3")
    elif opcion == 4:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 3")
 
print ("Fin")
    

