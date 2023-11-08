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