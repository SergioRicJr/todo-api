from todo.utils.random_hash import make_random_hash

def test_make_random_hash_length():
    hash_value = make_random_hash()
    assert len(hash_value) == 64

def test_make_random_hash_uniqueness():
    hash1 = make_random_hash()
    hash2 = make_random_hash()
    assert hash1 != hash2