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
        """ Returns a dictionary of all cities with a state_id
            matching this instance's id
        """
        from models.__init__ import storage

        # Create empty dictionary
        c_dict = {}

        # Fill with all cities whose state_id match this instance's id
        for key, value in storage.all(City).items():
            if value.to_dict()['state_id'] == self.id:
                c_dict[key] = value
