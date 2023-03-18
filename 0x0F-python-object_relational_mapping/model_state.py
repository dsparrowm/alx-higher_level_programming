#!/usr/bin/python3
"""
a python file that contains the class definition of a State
and an instance Base = declarative_base():
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
        Class that links to the states table
    """
    __table__name = 'states'
    id = Column(Integer, Primary_Key=True)
    name = Column(String(128), nullable=False)
