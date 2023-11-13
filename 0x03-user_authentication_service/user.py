#!/usr/bin/env python3
"""Defines the User class Model for the users table in the database
"""
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class User(Base):
    """Representation of a user instance in the database
    """
    pass
