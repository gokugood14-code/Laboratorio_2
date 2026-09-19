"""Demostración de paso de parámetros (Req. 8) y alcance de variables (Req. 9)."""


def sumar_un_anio(edad):
    """Recibe un número (tipo inmutable): trabaja con una COPIA del dato."""
    edad = edad + 1
    return edad


def agregar_elemento(lista, elemento):
    """Recibe una lista (tipo mutable): modifica la lista ORIGINAL."""
    lista.append(elemento)


def probar_paso_de_parametros():
    edad = 20
    print(f"Antes de llamar a la función   : edad = {edad}")
    nueva_edad = sumar_un_anio(edad)
    print(f"La función devolvió            : {nueva_edad}")
    print(f"Después de llamar a la función : edad = {edad}   (el original no cambió)")

    solicitudes = ["S1"]
    print(f"\nAntes de llamar a la función   : solicitudes = {solicitudes}")
    agregar_elemento(solicitudes, "S2")
    print(f"Después de llamar a la función : solicitudes = {solicitudes}   (la lista original sí cambió)")


if __name__ == "__main__":
    probar_paso_de_parametros()