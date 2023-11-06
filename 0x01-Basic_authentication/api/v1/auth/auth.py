#!/usr/bin/env python3
"""Authentication module for v1 API.
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ Auth class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Checks if a request to a given path requires authentication or not.

        Args:
            path (str): The path of the request.
            excluded_paths (List[str]): A list of paths that do not require
                                        authentication.

        Returns:
            bool: True if authentication is required, False otherwise.
        """
        pass

    def authorization_header(self, request=None) -> str:
        pass

    def current_user(self, request=None) -> TypeVar('User'):
        pass
