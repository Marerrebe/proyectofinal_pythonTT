"""
Funciones de validación reutilizable en el sistema 
"""

def validar_str(mensaje:str, campo: str = "campo") -> str:
    """
    pide un texto al usuario y repite hasta que no esté vacío.

    """
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print(f" el {campo} no puede estar vacio. Intenta de nuevo.")

def validar_float(mensaje:str, minimo: float = 0.0) -> float:
    """
    Pide un numero decimal al usuario y repite hasta que sea valido
    """
    while True:
        entrada = input(mensaje).strip()
        try:
            valor = float(entrada)
            if valor < minimo:
                print(f" El valor debe er mayor o igual a {minimo}.")
            else:
                return valor
        except ValueError:
            print(f" {entrada} no es un numero valido. intentalo denuevo")

def validar_int(mensaje:str, minimo: int = 1) -> int:
    """
    Pide un numero entero al usuario y repite hasta que sea valido
    """
    while True:
        entrada = input(mensaje).strip()
        try:
            valor = int(entrada)
            if valor < minimo:
                print(f" El valor debe ser mayor o igual a {minimo}.")
            else:
                return valor
        except ValueError:
            print(f" {entrada} no es un numero valido. intentalo denuevo")

def preguntar_si_no(mensaje:str) -> bool:
    while True:
        respuesta = input(f"{mensaje} (s/n): ").strip().lower()
        if respuesta == "s":
            return True
        elif respuesta == "n":
            return False
        else:
            print("  ❌ Ingresá 's' para sí o 'n' para no.")

