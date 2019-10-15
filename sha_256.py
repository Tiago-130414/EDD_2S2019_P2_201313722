import hashlib

class encriptacion(self):
    def encriptar(self,hash_cadena):
        sha_asignacion = hashlib.sha256(hash_cadena.encode()).hexdigest()
        return sha_asignacion
