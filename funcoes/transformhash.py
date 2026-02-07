import hashlib

def transformar_hash(valor):
    algoritmo = hashlib.sha256()
    algoritmo.update(valor.encode())
    return algoritmo.hexdigest()


