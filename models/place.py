#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from os import getenv

place_amenity = Table("place_amenity", Base.metadate,
                      Column("place_id", String(60), nullable=False,
                             ForeignKey("places.id"), primary_key=True),
                      Column("amenity_id", String(60), nullable=False,
                             ForeignKey("amenities.id"), primary_key=True)
                      )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"

    city_id = Column(String(60), nullable=False, ForeignKey('cities.id'))
    user_id = Column(String(60), nullable=False, ForeignKey('users.id'))
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False, default=0)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=False, default=0)
    longitude = Column(Float, nullable=False, default=0)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") is "db":
        amenities = relationship("Amenity", secondary="place_amenities", viewonly=False)
    else:
        @property
        def amenities(self):
            """ Getter for amenities """
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj):
            """ Setter for amenities """
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
