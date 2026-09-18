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