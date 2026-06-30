"""
Guarda y carga products desde el disco.
"""
import json
import sqlite3
import os
import config
from datetime import datetime

ARCHIVO_JSON = config.ARCHIVO_JSON
ARCHIVO_ERRORES = config.ARCHIVO_ERRORES
ARCHIVO_DB = config.ARCHIVO_DB

#-------------------  LOG DE ERRORES EN TXT (.log)  ------------------
def registrar_error(mensaje:str) -> None:
    """
    Crea un registro de errores en archivo .log
    """
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # 2026-06-17
    linea = f"[{ahora}] {mensaje}\n"

    try:
        with open(ARCHIVO_ERRORES,"a",encoding="utf-8") as archivo:
            archivo.write(linea)
    except Exception as e:
        print(f"No se pudo escribir en el log: {linea.strip()}")
        print(f"El error es {e}")

# -------- SQL -------------
def obtener_conexion() -> sqlite3.Connection:
    conexion = sqlite3.connect(ARCHIVO_DB)
    conexion.row_factory = sqlite3.Row
    return conexion

def crear_tabla():
    sql = """
        CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        categoria TEXT NOT NULL,
        precio REAL NOT NULL
        )
    """
    try:
        with obtener_conexion() as con:
            con.execute(sql)
        return True
    except Exception as e:
        msg = f"[SQL] error al crear la tabla: {e}"
        print(f"{msg} - se usara JSON para reemplazo")
        registrar_error(msg)
        return False

def sql_obtener_todos() -> list:
    sql = "SELECT id, nombre, categoria, precio FROM productos ORDER BY id"
    with obtener_conexion() as con:
        return [dict(fila) for fila in con.execute(sql).fetchall()]

def sql_insertar(nombre: str, categoria: str, precio: float) -> dict:
    sql = "INSERT INTO productos (nombre, categoria, precio) VALUES (?, ?, ?)"
    with obtener_conexion() as con:
        cursor = con.execute(sql, (nombre, categoria, precio))
    # cursor = con.execute("INSERT INTO productos (nombre, categoria, precio) VALUES (?, ?, ?)",(nombre, categoria, precio))
        return {"id": cursor.lastrowid, "nombre": nombre, "categoria": categoria, "precio": precio}

def sql_eliminar(id_a_eliminar: int) -> bool:
    sql = "DELETE FROM productos WHERE id = ?"
    with obtener_conexion() as con:
        cursor = con.execute(sql, (id_a_eliminar,))
        return cursor.rowcount > 0

# --------- JSON --- -----

def guardar_json(productos: list) -> bool:
    """
    Sobrescribe el archivo JSON con la lista de productos.
    El archivo queda asi:
    [{},{},{}]
    """
    try:
        with open(ARCHIVO_JSON,"w",encoding="utf-8") as archivo:
            json.dump(productos, archivo, indent=4 , ensure_ascii=False)
        return True
    except PermissionError:
        msg = f"Sin permisos para escribir '{ARCHIVO_JSON}'"
        print(f"❌ {msg}")
        registrar_error(msg)
        return False
    except Exception as e:
        msg = f"Eror al guardar JSON: {e}"
        print(f"❌ {msg}")
        registrar_error(msg)
        return False

def cargar_json() -> list:
    """
    Lee el archivo json y deuelve la lista de productos
    """

    if not os.path.exists(ARCHIVO_JSON):
        return []

    try:
        with open(ARCHIVO_JSON,"r",encoding="utf-8") as archivo:
            datos = json.load(archivo)
        return datos
    except json.JSONDecodeError as e:
        msg = f"Archivo {ARCHIVO_JSON} corrupto: {e}"
        print(f" ❌ {msg}")
        registrar_error(msg)
        return []
    except Exception as e:
        msg = f"Error al cargar el json: {e}"
        print(f" ❌ {msg}")
        registrar_error(msg)
        return []

def proximo_id(productos: list) -> int:
    """
    Calcula el próximo ID disponible.
    Es el equivalente manual al AUTOINCREMENT de SQL.

    Args:
        productos (list): Lista actual de productos.

    Returns:
        int: El próximo ID a usar.
    """
    if not productos:
        return 1

    # Versión explícita, equivalente a: max(p["id"] for p in productos) + 1
    id_maximo = 0
    for p in productos:
        if p["id"] > id_maximo:
            id_maximo = p["id"]

    return id_maximo + 1

def obtener_todos() -> list:
    try:
        productos = sql_obtener_todos()
        print("datos cargados correctamente")
        return productos
    except Exception as e:
        registrar_error(f"obtener todo la base de SQLite fallo: {e}" )
        print("SQLite no funcionam, usarando json")
        return cargar_json()

