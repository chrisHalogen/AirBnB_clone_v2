#!/usr/bin/python3
"""
State Module for HBNB project
"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
import models
import shlex


class State(BaseModel, Base):
    """
    The state class
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        all_cities = models.storage.all()
        collect = []
        output = []
        for key in all_cities:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                collect.append(all_cities[key])
        for item in collect:
            if (item.state_id == self.id):
                output.append(item)
        return (output)
