#!/bin/python3

"""
Test suite for MockAPI class.
"""

from mock import MockAPI
import unittest

class NoFilenameInitTestCase(unittest.TestCase):
    def setUp(self):
        self.api = MockAPI()
        self.assertIsInstance(self.api, MockAPI)

    def test_datastore_empty(self):
        self.assertEqual(str(self.api), '{}')

    def test_get_data(self):
        self.assertEqual(self.api.get('1'), {})

class BadFilenameInitTestCase(unittest.TestCase):
    def setUp(self):
        self.api = MockAPI('data/test/notfound.txt')
        self.assertIsInstance(self.api, MockAPI)

    def test_datastore_empty(self):
        self.assertEqual(str(self.api), '{}')

class InvalidJSONInitTestCase(unittest.TestCase):
    def setUp(self):
        self.api = MockAPI('data/test/invalid.json')
        self.assertIsInstance(self.api, MockAPI)

    def test_datastore_empty(self):
        self.assertEqual(str(self.api), '{}')

class GoodInitTestCase(unittest.TestCase):
    def setUp(self):
        self.api = MockAPI('data/test/valid.json')
        self.assertIsInstance(self.api, MockAPI)

    def test_datastore_empty_not_empty(self):
        self.assertNotEqual(str(self.api), '{}')

    def test_get_data_present(self):
        self.assertNotEqual(self.api.get('1'), {})

    def test_get_data_absent(self):
        self.assertEqual(self.api.get('2'), {})

if __name__ == '__main__':
    unittest.main()
