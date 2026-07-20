from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.exceptions import InvalidSignature
private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
public_key = private_key.public_key()
article = "The election was held on Monday."
signature = private_key.sign(article.encode(), ec.ECDSA(hashes.SHA256()))
article = "The election was held on Tuesday."
try:
    public_key.verify(signature, article.encode(), ec.ECDSA(hashes.SHA256()))
    print(" Signature is valid and article is authentic")
except InvalidSignature:
    print(" Signature invalid and article was tampered with")
