#!/usr/bin/env python3
"""This module contains views for session authentication.
"""
from typing import Tuple


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> Tuple[str, int]:
    """Log in a user using session authentication.
    Returns:
        Tuple containing a JSON representation of a User object and an
        HTTP status code.
    """
    pass