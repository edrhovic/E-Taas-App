import firebase_admin
from firebase_admin import credentials, auth, exceptions
from firebase_admin.auth import ExpiredIdTokenError, InvalidIdTokenError
from pathlib import Path
import os

firebase_path = os.getenv("FIREBASE_CREDENTIALS_PATH")
cred = credentials.Certificate(firebase_path)

if not firebase_admin._apps:
    firebase_admin.initialize_app(credential=cred)


def verify_firebase_token(id_token: str) -> dict | None:
    try:
        return auth.verify_id_token(id_token)
    except exceptions.FirebaseError as e:
        print("Firebase verification failed:", e)
        return None