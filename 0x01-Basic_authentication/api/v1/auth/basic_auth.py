#!/usr/bin/env python3
"""Basic Authentication module for v1 API.
"""
from .auth import Auth
import re


class BasicAuth(Auth):
    """define basic auth class
    """
    def extract_base64_authorization_header(
            self,
            authorization_header: str) -> str:
        """Extrac the Base64 part of auth header
        """
        if type(authorization_header) == str:
            pattern = r'Basic (?P<token>.+)'
            field_match = re.fullmatch(pattern, authorization_header.strip())
            if field_match is not None:
                return field_match.group('token')
        return None


    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str) -> str:
        pass