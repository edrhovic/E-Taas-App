from passlib.context import CryptContext
from jwt import encode, decode, PyJWTError

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    truncated = password.encode("utf-8")[:72].decode("utf-8", errors="ignore")
    return pwd_context.hash(truncated)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    truncated = plain_password.encode("utf-8")[:72].decode("utf-8", errors="ignore")
    return pwd_context.verify(truncated, hashed_password)

def create_access_token(data: dict, secret_key: str, algorithm: str) -> str:
    return encode(data, secret_key, algorithm=algorithm)

def decode_access_token(token: str, secret_key: str, algorithms: list) -> dict:
    try:
        return decode(token, secret_key, algorithms=algorithms)
    except PyJWTError:
        return None

def is_token_valid(token: str, secret_key: str, algorithms: list) -> bool:
    try:
        decode(token, secret_key, algorithms=algorithms)
        return True
    except PyJWTError:
        return False
