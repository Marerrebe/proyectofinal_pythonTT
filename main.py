import menu
import productos as prod
import persistencia as db

def accion_agregar(lista_productos: list) -> None:
    """Flujo completo para agregar uno o más productos"""
    while True:
        nuevo_id = db.proximo_id
def accion_ver():
    ...
def accion_buscar():
    ...
def accion_eliminar():
    ...
def main()-> None:
    """
    """
    
lista_productos = db.cargar_json()
    print(f"\n Sistema iniciado. {len (lista_productos)} producto(s) cargado(s)")
    while True:
        menu.mostrar_menu()
        opcion = menu.pedir_opcion()

        if opcion == "1":
            accion_agregar()
        elif opcion == "2":
            accion_ver()
        elif opcion == "3":
            accion_buscar()
        elif opcion == "4":
            accion_eliminar() #buscar funcion lamda 
        elif opcion == "5":
           print ("\n Hasta luego👋")
           break
        else:
            print ("\n Opcion invalida. Ingresa un numero del 1 al 5")


#if__name__ == "__main__": #buena practica para que el programa se ejecute por una unica vez.
   # main()