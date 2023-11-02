#!/usr/bin/env python3
"""bcrypt password hashing module"""
import bcrypt


def hash_password(password: str) -> bytes:
    """passowrd hashing function using bcrypt with random salt"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    pass