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
    not_found_res = {"error": "no user found for this email"}
    email = request.form.get('email')
    password = request.form.get('password')
    if email is None or len(email.strip()) == 0:
        return jsonify({"error": "email missing"}), 400
    if password is None or len(password.strip()) == 0:
        return jsonify({"error": "password missing"}), 400