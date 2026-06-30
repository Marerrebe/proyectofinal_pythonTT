import menu
import productos as prod
import persistencia as db

def accion_agregar(lista_productos: list) -> None:
    """Flujo completo para agregar uno o más productos."""
    while True:
        nuevo_id = db.proximo_id(lista_productos)
        nuevo    = prod.crear_producto(lista_productos, nuevo_id)

        if db.guardar_json(lista_productos):
            print(f"\n  ✅ '{nuevo['nombre']}' agregado y guardado (ID: {nuevo['id']}).")
        else:
            print("\n  ⚠️  Producto en memoria pero no se pudo guardar en disco.")

        if not menu.preguntar_continuar("agregar"):
            break


def accion_ver(lista_productos: list) -> None:
    """Muestra todos los productos."""
    print("\n  === LISTA DE PRODUCTOS ===")
    menu.mostrar_lista_productos(lista_productos)


def accion_buscar(lista_productos: list) -> None:
    """Flujo completo para buscar productos por nombre."""
    while True:
        termino     = menu.pedir_termino_busqueda()
        encontrados = prod.buscar_por_nombre(lista_productos, termino)

        if encontrados:
            print(f"\n  Se encontraron {len(encontrados)} resultado(s):")
            menu.mostrar_lista_productos(encontrados)
        else:
            print(f"\n  ⚠️  No se encontraron productos con '{termino}'.")

        if not menu.preguntar_continuar("buscar"):
            break


def accion_eliminar(lista_productos: list) -> None:
    """Flujo completo para eliminar un producto por ID."""
    if not lista_productos:
        print("\n  ⚠️  No hay productos para eliminar.")
        return

    menu.mostrar_lista_productos(lista_productos)

    while True:
        id_elegido = menu.pedir_id_eliminar()
        producto   = prod.buscar_por_id(lista_productos, id_elegido)

        if not producto:
            print(f"\n  ❌ No existe ningún producto con ID {id_elegido}.")
        else:
            print("\n  Producto encontrado:")
            menu.mostrar_producto(producto)

            if menu.confirmar_eliminacion(producto["nombre"]):
                prod.eliminar_por_id(lista_productos, id_elegido)
                db.guardar_json(lista_productos)
                print(f"\n  ✅ Producto eliminado correctamente.")
            else:
                print("\n  Operación cancelada.")

        if not menu.preguntar_continuar("eliminar"):
            break


def main() -> None:
    """
    """
    lista_productos = db.cargar_json()
    print(f"\n Sistema iniciado. {len(lista_productos)} producto(s) cargado(s).")
    while True:
        menu.mostrar_menu()
        opcion = menu.pedir_opcion()

        if opcion == "1":
            accion_agregar(lista_productos)
        elif opcion == "2":
            accion_ver(lista_productos)
        elif opcion == "3":
            accion_buscar(lista_productos)
        elif opcion == "4":
            accion_eliminar(lista_productos)
        elif opcion == "5":
            print("\n Gracias. Vuelva pronto 👋")
            break
        else:
            print("\n Opcion invalida. Igresa un nuemor del 1 al 5")

if __name__ == "__main__":
    main()