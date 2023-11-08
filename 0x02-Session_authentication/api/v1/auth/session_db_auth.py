#!/usr/bin/env python3
"""session db auth module
"""
from .session_exp_auth import SessionExpAuth


class SessionDBAuth(SessionExpAuth):
    """session suth with db
    """
    def create_session(self, user_id=None) -> str:
        """create and store session id for usercrea
        """
        session_id = super().create_session(user_id)
        if type(session_id) == str:
            kwargs = {
                'user_id': user_id,
                'session_id': session_id,
            }
            user_session = UserSession(**kwargs)
            user_session.save()
            return session_id
