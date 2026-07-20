from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.exceptions import InvalidSignature
private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
public_key = private_key.public_key()

article = "The election was held on Monday."
signature = private_key.sign(article.encode(), ec.ECDSA(hashes.SHA256()))
print(" Attack 1: Content Tampering ")
tampered_article = "The election was held on Monday."

try:
    public_key.verify(signature, tampered_article.encode(), ec.ECDSA(hashes.SHA256()))
    print("Verified : system didnt catch tampering!")
except InvalidSignature:
    print("Detected! Article was tampered with.")
print("Attack 2: Signature Replay ")
different_article = "The prime minister resigned today."

try:
    public_key.verify(signature, different_article.encode(), ec.ECDSA(hashes.SHA256()))
    print("Verified : system didnt catch tampering!")
except InvalidSignature:
    print("Detected! Signature does not match this article.")


print("Attack 3: Wrong Public Key")
fake_private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
fake_public_key = fake_private_key.public_key()

try:
    fake_public_key.verify(signature, article.encode(), ec.ECDSA(hashes.SHA256()))
    print("Verified: system didn't catch tampering!")
except InvalidSignature:
    print("Detected! Signature does not match this public key.")
print(" Attack 4: Impersonation ")
attacker_private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
attacker_public_key = attacker_private_key.public_key()

fake_signature = attacker_private_key.sign(article.encode(), ec.ECDSA(hashes.SHA256()))

try:
    public_key.verify(fake_signature, article.encode(), ec.ECDSA(hashes.SHA256()))
    print("Verified: system didn't catch tampering!")
except InvalidSignature:
    print("Detected! This signature was not made by the real publisher.")