#!/usr/bin/python3
"""Defines a module ``model_state`` that contains
   ``State`` class.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Defines the class ``State`` that inherit from ``Base``.
    Attributes:
    id: class Attribute, primary key
    name: class attribute string of 128 characters
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
