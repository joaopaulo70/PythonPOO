from hashlib import sha256

texto = 'Gafanhoto'
cod = texto.encode('utf-8')
hash = sha256(cod).hexdigest()
print(hash)
