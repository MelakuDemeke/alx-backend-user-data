#!/usr/bin/env python3
"""Session Authentication module for v1 API.
"""
from flask import request

from .auth import Auth
from uuid import uuid4

class SessionAuth(Auth):
    """define Session auth class
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """create session with id for user
        """
        if type(user_id) is str:
            session_id = str(uuid4())
            self.user_id_by_session_id[session_id] = user_id
            return session_id
