#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("Child", cascade="delete-orphan", backref="state")

    @property
    def cities(self):
        """ Returns a list? dictionary? of all cities with a state_id
            matching this instance's id
        """
        