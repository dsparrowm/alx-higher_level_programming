#!/usr/bin/python3
"""Defines a module ``relationship_city`` that contains
   ``city`` class.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """Defines the class ``City`` that inherit from ``Base``.
    Attributes:
    id: class Attribute, primary key, Integer type
    name: class attribute, string of 128 characters, String
    state_id: class attribute, foreignKey to state id, Integer
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
