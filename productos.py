"""
Logica de negocio del sistema
"""
from utils import validar_str , validar_float

def crear_producto(productos: list, proximo_id: int) -> dict:
    """
    Pide los datos del nuevo producto al usuario y lo agrega a la lista.

    Args:
        productos   (list): Lista en memoria donde se agrega el producto.
        proximo_id  (int):  ID que se asignará al nuevo producto.

    Returns:
        dict: El producto recién creado.
    """
    print("\n  --- Nuevo producto ---")
    nombre    = validar_str("  Nombre    : ", campo="nombre")
    categoria = validar_str("  Categoría : ", campo="categoría")
    precio    = validar_float("  Precio    : $", minimo=0.01)

    producto = {
        "id":        proximo_id,
        "nombre":    nombre,
        "categoria": categoria,
        "precio":    precio,
    }
    productos.append(producto)
    return producto

def buscar_por_nombre(productos: list, termino: str) -> list:
    """
    Busca productos cuyo nombre contenga el término (sin distinguir mayúsculas).

    Args:
        productos (list): Lista completa de productos.
        termino   (str):  Texto a buscar.

    Returns:
        list: Lista (puede estar vacía) con los productos que coinciden.
    """
    termino_lower = termino.lower()
    # en una linea 
    # return [p for p in productos if termino_lower in p["nombre"].lower()]
    resultados = []

    for p in productos:
        if termino_lower in p["nombre"].lower():
            resultados.append(p)

    return resultados

def buscar_por_id(productos: list, id_buscado: int) -> dict | None:
    """
    Devuelve el producto con ese ID, o None si no existe.

    Args:
        productos  (list): Lista completa de productos.
        id_buscado (int):  ID a buscar.

    Returns:
        dict | None: El producto encontrado, o None.
    """
    for producto in productos:
        if producto["id"] == id_buscado:
            return producto
    return None

def eliminar_por_id(productos: list, id_a_eliminar: int) -> bool:
    """
    Elimina el producto con el ID indicado de la lista en memoria.

    Args:
        productos       (list): Lista completa de productos.
        id_a_eliminar   (int):  ID del producto a eliminar.

    Returns:
        bool: True si se encontró y eliminó, False si no existía.
    """
    for i, producto in enumerate(productos):
        if producto["id"] == id_a_eliminar:
            productos.pop(i)
            return True
    return False
