from passlib.hash import pbkdf2_sha256

def hash_password(password) -> str:
    """Hash a password for storing."""
    return pbkdf2_sha256.hash(password)

def verify_password(password, hash) -> bool:
    """Verify a stored password against one provided by user. Return True if matched, False otherwise."""
    return pbkdf2_sha256.verify(password, hash)
