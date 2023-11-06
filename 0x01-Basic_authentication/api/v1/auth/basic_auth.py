#!/usr/bin/env python3
"""Basic Authentication module for v1 API.
"""
from .auth import Auth


class BasicAuth(Auth):
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        pass