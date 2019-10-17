import hashlib

def encriptar(cadena):
    sha_asignacion = hashlib.sha256(cadena.encode()).hexdigest()
    return sha_asignacion
