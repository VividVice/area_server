from passlib.hash import pbkdf2_sha256
from os import getenv
from random import randbytes, seed, random
import string
def hash_password(password) -> str:
    """Hash a password for storing."""
    return pbkdf2_sha256.hash(password)

def verify_password(password, hash) -> bool:
    """Verify a stored password against one provided by user. Return True if matched, False otherwise."""
    return pbkdf2_sha256.verify(password, hash)

def generate_username(invalid_usernames:set, len =10, seed_val=0) -> str:
    def random_string(length):
        """Generate a random string of fixed length."""
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    """Generate a unique username"""
    if seed_val != 0:
        seed(seed_val)
    username = random_string(len)
    if username in invalid_usernames:
        return generate_username(invalid_usernames, len, seed_val+1)
    return username