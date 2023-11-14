#!/usr/bin/env python3
"""Flask app for User Authentication Service
"""
from flask import Flask, jsonify
app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def index() -> str:
    """GET /
    Return:
        - This function returns the home page's payload as a JSON object
    """
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
