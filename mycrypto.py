from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.exceptions import InvalidSignature

def sign_article(article):
    private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
    public_key = private_key.public_key()
    signature = private_key.sign(article.encode(), ec.ECDSA(hashes.SHA256()))
    
    from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
    public_key_hex = public_key.public_bytes(Encoding.DER, PublicFormat.SubjectPublicKeyInfo).hex()
    
    return {
        "signature": signature.hex(),
        "public_key": public_key_hex,
        "message": "Article signed successfully!"
    }
def verify_article(article, signature, public_key):
    try:
        from cryptography.hazmat.primitives.serialization import load_der_public_key
        pub_key = load_der_public_key(bytes.fromhex(public_key))
        pub_key.verify(
            bytes.fromhex(signature),
            article.encode(),
            ec.ECDSA(hashes.SHA256())
        )
        return {"result": "valid", "message": "✓ Article is authentic!"}
    except InvalidSignature:
        return {"result": "invalid", "message": "✗ Article was tampered with!"}
def simulate_attacks(article, signature, public_key):
    from cryptography.hazmat.primitives.serialization import load_der_public_key, Encoding, PublicFormat
    pub_key = load_der_public_key(bytes.fromhex(public_key))
    results = []

    
    tampered = article + " TAMPERED"
    try:
        pub_key.verify(bytes.fromhex(signature), tampered.encode(), ec.ECDSA(hashes.SHA256()))
        results.append({"attack": "Content Tampering", "detected": False})
    except InvalidSignature:
        results.append({"attack": "Content Tampering", "detected": True})

  
    different_article = "This is a completely different article."
    try:
        pub_key.verify(bytes.fromhex(signature), different_article.encode(), ec.ECDSA(hashes.SHA256()))
        results.append({"attack": "Signature Replay", "detected": False})
    except InvalidSignature:
        results.append({"attack": "Signature Replay", "detected": True})

    fake_private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
    fake_public_key = fake_private_key.public_key()
    fake_pub_hex = fake_public_key.public_bytes(Encoding.DER, PublicFormat.SubjectPublicKeyInfo).hex()
    fake_pub = load_der_public_key(bytes.fromhex(fake_pub_hex))
    try:
        fake_pub.verify(bytes.fromhex(signature), article.encode(), ec.ECDSA(hashes.SHA256()))
        results.append({"attack": "Wrong Public Key", "detected": False})
    except InvalidSignature:
        results.append({"attack": "Wrong Public Key", "detected": True})


    attacker_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
    fake_signature = attacker_key.sign(article.encode(), ec.ECDSA(hashes.SHA256()))
    try:
        pub_key.verify(fake_signature, article.encode(), ec.ECDSA(hashes.SHA256()))
        results.append({"attack": "Impersonation", "detected": False})
    except InvalidSignature:
        results.append({"attack": "Impersonation", "detected": True})

    return results
