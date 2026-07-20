import hashlib
article="The election was held on Tuesday."
fingerprint= hashlib.sha256(article.encode()).hexdigest()
print(fingerprint)