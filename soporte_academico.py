"""Sistema de orientación y registro de atenciones - Soporte Académico."""


def registrar_solicitud(codigo, nombre, tipo, descripcion):
    """Req. 1: arma la solicitud con los datos básicos y la devuelve."""
    solicitud = {
        "codigo": codigo.strip(),
        "nombre": nombre.strip(),
        "tipo": tipo.strip().lower(),
        "descripcion": descripcion.strip(),
    }
    return solicitud


def mostrar_menu():
    """Req. 4: muestra el menú principal (función sin retorno)."""
    print("\n === SOPORTE ACADÉMICO ===")
    print("1. Registrar solicitud")
    print("2. Ver solicitudes registradas")
    print("3. Salir")


def validar_codigo(codigo, longitud_minima):
    """Req. 2: True si el código no está vacío y alcanza la longitud mínima."""
    codigo_limpio = codigo.strip()
    return codigo_limpio != "" and len(codigo_limpio) >= longitud_minima