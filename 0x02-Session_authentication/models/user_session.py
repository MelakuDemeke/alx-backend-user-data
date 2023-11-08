#!/usr/bin/env python3
"""This module defines the UserSession class, which represents
a user session in the application.
"""
from models.base import Base


class UserSession(Base):
    """User session class
    """

    def __init__(self, *args: list, **kwargs: dict):
        """initializes a UserSession object
        """
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
