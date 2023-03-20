#!/usr/bin/python3
"""Defines a module ``relationship_state.py`` that contains
   ``State`` class.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import City, Base


class State(Base):
    """Defines the class ``State`` that inherit from ``Base``.
    Attributes:
    id: class Attribute, primary key
    name: class attribute string of 128 characters
    cities: class attribute, linkes to ``city`` class
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all, delete-orphan")
