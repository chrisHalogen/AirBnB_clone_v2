#!/usr/bin/python3
""" 
A New Class for SQL Alchemy
"""
from os import getenv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session

from sqlalchemy.ext.declarative import declarative_base
from models.user import User
from models.base_model import BaseModel as Base
from models.place import Place
from models.state import State
from models.review import Review
from models.city import City
from models.amenity import Amenity

class DBStorage:
    """
    Creates Tables in the Database
    """
    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        env = getenv("HBNB_ENV")
        passwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'
            .format(user, passwd, host, db),
            pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, model_type=None):
        """
        Returns A Dictionary of Objects of class model_type
        """
        output = {}
        if model_type:
            if type(model_type) is str:
                model_type = eval(model_type)
            query = self.__session.query(model_type)
            for item in query:
                key = "{}.{}".format(type(item).__name__, item.id)
                output[key] = item
        else:
            models = [State, City, User, Place, Review, Amenity]
            for model in models:
                query = self.__session.query(model)
                for item in query:
                    key = "{}.{}".format(type(item).__name__, item.id)
                    output[key] = item
        return (output)

    def new(self, obj):
        """
        Create new element in db
        """
        self.__session.add(obj)

    def save(self):
        """
        commit changes to db
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        remove element from db
        """
        if obj:
            self.session.delete(obj)

    def reload(self):
        """
        reload configuration
        """
        Base.metadata.create_all(self.__engine)
        sesn = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sesn)
        self.__session = Session()

    def close(self):
        """
        close session
        """
        self.__session.close()
