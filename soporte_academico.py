"""Sistema de orientación y registro de atenciones - Soporte Académico."""
import unicodedata

def registrar_solicitud(codigo, nombre, tipo, descripcion):
    """Req. 1 y 5: arma la solicitud (con su prioridad) y la devuelve."""
    solicitud = {
        "codigo": codigo.strip(),
        "nombre": nombre.strip(),
        "tipo": normalizar_texto(tipo),
        "descripcion": descripcion.strip(),
        "prioridad": asignar_prioridad(tipo),
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


def normalizar_texto(texto):
    """Apoyo de Req. 3 y 5: minúsculas, sin espacios en los extremos y sin tildes."""
    texto_limpio = texto.strip().lower()
    descompuesto = unicodedata.normalize("NFD", texto_limpio)  # separa la letra de su tilde
    return "".join(letra for letra in descompuesto if unicodedata.category(letra) != "Mn")


def validar_tipo_consulta(tipo, tipos_validos):
    """Req. 3: True si el tipo de consulta pertenece a la lista básica."""
    tipo_normalizado = normalizar_texto(tipo)
    return tipo_normalizado in tipos_validos


def validar_texto_obligatorio(texto):
    """Req. 6: True si el texto tiene contenido (no está vacío ni solo con espacios)."""
    texto_limpio = texto.strip()
    return texto_limpio != ""


def asignar_prioridad(tipo):
    """Req. 5: devuelve "Alta", "Media" o "Baja" según el tipo de consulta."""
    tipo_normalizado = normalizar_texto(tipo)
    if tipo_normalizado in ("plataforma", "matricula"):
        prioridad = "Alta"
    elif tipo_normalizado == "pagos":
        prioridad = "Media"
    else:
        prioridad = "Baja"
    return prioridad


def mostrar_resumen(solicitud):
    """Req. 7: muestra en pantalla el resumen de una solicitud registrada."""
    print("--- Resumen de la solicitud ---")
    print(f"Código      : {solicitud['codigo']}")
    print(f"Nombre      : {solicitud['nombre']}")
    print(f"Tipo        : {solicitud['tipo']}")
    print(f"Descripción : {solicitud['descripcion']}")
    print(f"Prioridad   : {solicitud['prioridad']}")