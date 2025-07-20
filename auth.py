# Auth and JWT utilities
from datetime import datetime, timedelta, timezone # Used to create token expiry times

import jwt # Encoding and decoding tokens.
from passlib.context import CryptContext #Used to hash and verify passwords
from .models import UserInDB

SECRET_KEY = "b7ab64808b6c4fbe145f55659266c8a6233381644a330b67d87c4945c7144b31" # Used when creating and decoding tokens. It must be consistent while creating and decoding a token.
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=['bcrypt'], depracated='auto') # We are using bcrypt algorithm for hashing. CryptContext manages hashing and verification securely. Automatically handles algorithm changes in future.

# Utility for Hashing a new password
'''
The function converts plain password into bcrypt hash
This is what will be stored in the database.
Hashing is ONE-WAY. You can't reverse it.
Usage: during user registration
'''
def get_password_hash(password):
    return pwd_context.hash(password)


# Utility for password verification
'''
The function takes in plain password and hashed password.
It then uses bcrypt to securely compares the two passwords
It then returns TRUE if they match.
Usage: During login to check if user provided password matches the one in the DB.
'''
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


