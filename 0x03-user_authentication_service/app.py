#!/usr/bin/env python3
"""Flask app for User Authentication Service
"""
from flask import Flask, jsonify, request
from auth import Auth
app = Flask(__name__)

AUTH = Auth()


@app.route("/", methods=["GET"], strict_slashes=False)
def index() -> str:
    """GET /
    Return:
        - This function returns the home page's payload as a JSON object
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def users() -> str:
    """POST /users
    Return:
        - new user's payload as a JSON object
    """
    email, password = request.form.get("email"), request.form.get("password")
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login() -> str:
    """POST /sessions
    Return:
        - new session ID as a JSON object
    """
    pass


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
