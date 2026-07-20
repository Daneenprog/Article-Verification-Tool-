from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
privatekey = ec.generate_private_key(ec.SECP256R1(), default_backend())
publickey=privatekey.public_key()
article = "The election was held on Monday."
signature = privatekey.sign(article.encode(), ec.ECDSA(hashes.SHA256()))
print("Article signed!")
print(signature.hex())




