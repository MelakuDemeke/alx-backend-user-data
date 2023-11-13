#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a new user to the database
        """
        try:
            user_to_add = User(email=email, hashed_password=hashed_password)
            self._session.add(user_to_add)
            self._session.commit()
        except Exception:
            self._session.rollback()
            user_to_add = None
        return user_to_add

    def find_user_by(self, **kwargs) -> User:
        """Finds a user in the database based on the provided keyword arguments
        """
        filter_fields = []
        filter_values = []
        for filter_key, filter_value in kwargs.items():
            if hasattr(User, filter_key):
                filter_fields.append(getattr(User, filter_key))
                filter_values.append(filter_value)

