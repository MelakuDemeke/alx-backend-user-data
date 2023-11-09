#!/usr/bin/env python3
"""This module contains views for session authentication.
"""
from typing import Tuple
from models.user import User
from flask import abort, jsonify, request
import os
from api.v1.views import app_views


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
    try:
        users = User.search({'email': email})
    except Exception:
        return jsonify(not_found_res), 404
    if len(users) <= 0:
        return jsonify(not_found_res), 404
    if users[0].is_valid_password(password):
        from api.v1.app import auth
        sessiond_id = auth.create_session(getattr(users[0], 'id'))
        res = jsonify(users[0].to_json())
        res.set_cookie(os.getenv("SESSION_NAME"), sessiond_id)
        return res
    return jsonify({"error": "wrong password"}), 401


@app_views.route(
    '/auth_session/logout', methods=['DELETE'], strict_slashes=False)
def logout() -> Tuple[str, int]:
    """
    Logs out the current user by destroying their session.

    Returns:
        A tuple containing an empty JSON response and a status code of 200.
        If the session could not be destroyed, returns a 404 error.
    """
    from api.v1.app import auth
    is_destroyed = auth.destroy_session(request)
    if not is_destroyed:
        abort(404)
    return jsonify({})
