#!/usr/bin/env python3
"""Authentication module for v1 API.
"""
from flask import request


class Auth:
    """ Auth class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        pass
