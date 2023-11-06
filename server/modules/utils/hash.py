from passlib.hash import pbkdf2_sha256
from os import getenv
from random import randbytes, seed
def hash_password(password) -> str:
    """Hash a password for storing."""
    return pbkdf2_sha256.hash(password)

def verify_password(password, hash) -> bool:
    """Verify a stored password against one provided by user. Return True if matched, False otherwise."""
    return pbkdf2_sha256.verify(password, hash)

def server_encrypt(data) -> str:
    """Encrypt data with a key."""
    return pbkdf2_sha256.hash(data, salt=getenv('SERVER_SECRET_KEY'))

def server_decrypt(data) -> bool:
    """Decrypt data with a key."""
    return pbkdf2_sha256.verify(data, salt=getenv('SERVER_SECRET_KEY'))

def generate_username(invalid_usernames:set, len =10, seed_val=0) -> str:
    """Generate a unique username"""
    if seed_val != 0:
        seed(seed_val)
    username = randbytes(len).hex()
    if username in invalid_usernames:
        return generate_username(invalid_usernames, len, seed_val+1)
    return username