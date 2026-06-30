"""
Responsabilidad: mostrar informacion en consola y pedir al usuario

este modulo no tiene logica de negocio ni acceso a archivos externos.
"""
import utils

def mostrar_menu() -> None:
    """ Muestra del menu """
    print("\n" + "=" * 50)
    print("             SISTEMA DE GESTION DE PRODUCTOS ")
    print("=" * 50)
    print("1. Agregar producto")
    print("2. Ver producto")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")
   

def pedir_opcion() -> str:
    """ pide y devuelve una opcion elegida por un usuario"""
    return input("Seleccione una opcion (1-5): ")

def preguntar_continuar(accion: str) -> bool:
    """
    
    """
    return utils.preguntar_si_no(f"¿Queres {accion} otro producto?")

def mostrar_producto(producto: dict) -> None:
    """
    Muestra los datos de un producto.
    """
    print(f"ID   : {producto["id"]}")
    print(f"nombre   : {producto["nombre"]}")
    print(f"categoria   : {producto["categoria"]}")
    print(f"precio   : {producto["precio"]}")

def mostrar_lista_productos(productos: list) -> None:
    """
    Muestra todos los productos en formato tabla

    Args:
        productos (list): lista de diccionarios con los productos.
    """
    if not productos:
        print("\n No hay productos cargados.")
        return

    print("\n" + "-" * 55)
    print(f" {'ID':<5} {'NOMBRE':<20} {'CATEGORIA' :<15} {'PRECIO':>10}")
    print("\n" + "-" * 55)

    for p in productos:
        print(f"{p['id']:<5} {p['nombre']:<20} {p['categoria']:<15} ${p['precio']:>10}")
    print("-" *55)
    print(f" Total de productos: {len(productos)}")

def pedir_id_eliminar() -> int:
    """
    Pide el ID del producto a eliminar
    """
    return utils.validar_int(f"\nIngresá el ID del producto a eliminar: ",minimo=1)

def confirmar_eliminacion(nombre:str) -> bool:
    """
    Pide confirmacion antes de eliminar un producto
    """
    return utils.preguntar_si_no(f"\n¿Confirmas que queres eliminar '{nombre}'? ")

def pedir_termino_busqueda() -> str:
    """
    Pide el termino de busqueda al usuarios
    """
    return utils.validar_str("\n Ingresa el nombre a buscar: ", campo="término de busqueda")


 
