#!/bin/python3

import json

class MockAPI:
    """Base class to mimic health insurance API functionality."""

    def __init__(self, filename=None):
        """Initialize datastore, optionally load from file."""
        self.data = {}
        if filename: self._read(filename)

    def __str__(self):
        """Return datastore as string."""
        return str(self.data)

    def _read(self, filename):
        """Method to load member data from JSON file,
        prints error msg on failure.
        """
        try:
            with open(filename, 'r') as file:
                self.data = json.loads(file.read())
        except Exception as ex:
            print('Error reading from file:', ex)

    def get(self, member_id) -> dict:
        """Method to access health insurance data using member_id,
        returns empty dict if member_id not found.
        """
        return self.data.get(member_id, {})

class MockAPI1(MockAPI):
    """Mock health insurance API 1."""

    def __init__(self):
        """Initialize datastore from file."""
        super().__init__('data/data1.json')

class MockAPI2(MockAPI):
    """Mock health insurance API 2."""

    def __init__(self):
        """Initialize datastore from file."""
        super().__init__('data/data2.json')

class MockAPI3(MockAPI):
    """Mock health insurance API 3."""

    def __init__(self):
        """Initialize datastore from file."""
        super().__init__('data/data3.json')
