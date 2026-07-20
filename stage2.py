import hashlib

original = "The election was held on Monday."
original_hash = hashlib.sha256(original.encode()).hexdigest()

received = "The election was held on Tuesday."
received_hash = hashlib.sha256(received.encode()).hexdigest()

if original_hash == received_hash:
    print("Article is unchanged")
else:
    print("Article was tampered with!")