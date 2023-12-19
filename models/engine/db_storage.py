#!/usr/bin/python3
""" new class for sqlAlchemy """
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.amenity import Amenity
from models.state import State
from models.place import Place
from models.review import Review
from models.user import User
from models.city import City

class DBStorage:
    """
    Database management
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Instantiates the class.
        Creates a DB COnnection
        """
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, class_=None):
        """
        Returns a dictionary of all the objects
        if class_ is not none, then it returns
        objects from that class alone
        """
        output = {}
        if class_:
            if type(class_) is str:
                class_ = eval(class_)
            query = self.__session.query(class_)
            for elem in query:
                key = "{}.{}".format(type(elem).__name__, elem.id)
                output[key] = elem
        else:
            classes = [State, City, User, Place, Review, Amenity]
            for cls in classes:
                query = self.__session.query(cls)
                for elem in query:
                    key = "{}.{}".format(type(elem).__name__, elem.id)
                    output[key] = elem
        return (output)

    def new(self, obj):
        """
        Creates new entry in DB
        """
        self.__session.add(obj)

    def save(self):
        """
        commits changes to db
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        removes element from db if the obj is not none
        """
        if obj:
            self.session.delete(obj)

    def reload(self):
        """
        reload session configurations
        """
        Base.metadata.create_all(self.__engine)
        sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sec)
        self.__session = Session()

    def close(self):
        """
        close connection
        """
        self.__session.close()
