#!/usr/bin/python3
"""
Contains all about test_db storage
"""
from datetime import datetime
import inspect
import models
import json
import os
import pycodestyle
import unittest
from models.engine import db_storage
from models.review import Review
from models.amenity import Amenity
from models.city import City
from models.base_model import BaseModel
from models.place import Place
from models.user import User
from models.state import State

DBStorage = db_storage.DBStorage
classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}
storage_t = os.getenv("HBNB_TYPE_STORAGE")


class TestDBStorageDocs(unittest.TestCase):
    """
    Tests the documentation and style
    """
    @classmethod
    def setUpClass(mdl):
        """
        Setting up for the docs test
        """
        mdl.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_conformance_db_storage(self):
        """
        models/engine/db_storage.py follows PEP8 style
        """
        pep8s = pycodestyle.StyleGuide(quiet=True)
        output = pep8s.check_files(['models/engine/db_storage.py'])
        self.assertEqual(output.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_db_storage(self):
        """
        tests/test_models/test_db_storage.py follows PEP8 style
        """
        pep8s = pycodestyle.StyleGuide(quiet=True)
        output = pep8s.check_files(['tests/test_models/test_engine/\
test_db_storage.py'])
        self.assertEqual(output.total_errors, 0,
                         "Found code style errors (and warnings).")

class TestDBStorageDocs(unittest.TestCase):
    """
    DBStorage class - Checking Docs and Style
    """
    @classmethod
    def setUpClass(mdl):
        """
        Setting up for the tests
        """
        mdl.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_conformance_db_storage(self):
        """
        models/engine/db_storage.py follows PEP8
        """
        pep8s = pycodestyle.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_db_storage(self):
        """
        tests/test_models/test_db_storage.py follow PEP8 style
        """
        pep8s = pycodestyle.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_engine/\
test_db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_db_storage_module_docstring(self):
        """
        db_storage.py module docstring
        """
        self.assertIsNot(db_storage.__doc__, None,
                         "db_storage.py needs a docstring")
        self.assertTrue(len(db_storage.__doc__) >= 1,
                        "db_storage.py needs a docstring")

    def test_db_storage_class_docstring(self):
        """
        DBStorage class docstring
        """
        self.assertIsNot(DBStorage.__doc__, None,
                         "DBStorage class needs a docstring")
        self.assertTrue(len(DBStorage.__doc__) >= 1,
                        "DBStorage class needs a docstring")

    def test_dbs_func_docstrings(self):
        """
        DBStorage methods docstring
        """
        for func in self.dbs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestFileStorage(unittest.TestCase):
    """
    FileStorage class tests
    """
    @unittest.skipIf(storage_t != 'db', "not testing db storage")
    def test_all_returns_dict(self):
        """
        Test for dict output
        """
        self.assertIs(type(models.storage.all()), dict)

    @unittest.skipIf(storage_t != 'db', "not testing db storage")
    def test_all_no_class(self):
        """
        All returns all rows when class is empty
        """

    @unittest.skipIf(storage_t != 'db', "not testing db storage")
    def test_new(self):
        """
        New adds entry to db
        """

    @unittest.skipIf(storage_t != 'db', "not testing db storage")
    def test_save(self):
        """
        Save commits to json
        """
