import secrets

def make_random_hash(size=32):
    return secrets.token_hex(size)
