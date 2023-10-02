import datetime
from jose import jwt
from os import getenv

def createToken(username: str, Long:bool) -> str:
    """Create a JWS token for a given username."""
    payload = {
        'username': username,
        'exp': datetime.datetime.utcnow() + (datetime.timedelta(minutes=30) if not Long else datetime.timedelta(days=30))
    }
    secret = getenv('SERVER_SECRET_KEY')
    print(secret)
    algorithm = 'HS256'
    token = jwt.encode(payload, secret, algorithm=algorithm)
    return token

def decodeToken(token: str) -> dict:
    """Decode a JWS token and return the payload."""
    return jwt.decode(token, getenv('SERVER_SECRET_KEY'), algorithms=['HS256'])