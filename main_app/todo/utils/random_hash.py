import hashlib
import random
import string

def make_random_hash(size=32):
    caracteres = string.ascii_letters + string.digits
    random_hash = ''.join(random.choice(caracteres) for _ in range(size))
    random_hash = hashlib.sha256(random_hash.encode()).hexdigest()
    return random_hash