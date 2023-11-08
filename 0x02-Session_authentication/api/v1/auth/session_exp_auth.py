#!/usr/bin/env python3
"""provides functionality for session authentication with expiration
"""
import os
from .session_auth import SessionAuth


class SessionExpAuth(SessionAuth):
    """Inherits from SessionAuth and addssession expiration functionality.
    """
    def __init__(self) -> None:
        """init new session Exp auth
        """
        super().__init__()
        try:
            self.session_duration = int(os.getenv('SESSION_DURATION', '0'))
        except Exception:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """new session id for new user
        """
        session_id = super().create_session(user_id)
        if type(session_id) != str:
            return None
        self.user_id_by_session_id[session_id] = {
            'user_id': user_id,
            'created_at': datetime.now(),
        }
        return session_id