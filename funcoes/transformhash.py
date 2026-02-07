import hashlib

def transformar_hash(valor):
    algoritimo = hashlib.sha256()
    algoritimo.update(valor.encode())
    return algoritimo.hexdigest()


