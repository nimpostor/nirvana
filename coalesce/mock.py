#!/bin/python3

"""
Three mock APIs for retreiving health insurance member data.
"""

import json

class MockAPI:
    """Base class for common health insurance API functionality."""

    def __init__(self, filename=None):
        """Initialize datastore, optionally load from file."""
        self.data = {}
        if filename: self._read(filename)

    def __str__(self):
        """Return datastore as string."""
        return str(self.data)

    def _read(self, filename):
        """Load member data from JSON file. For internal use only."""
        try:
            with open(filename, 'r') as file:
                self.data = json.loads(file.read())
        except Exception as ex:
            print('Error reading from file:', ex)

    def get(self, member_id: str) -> dict:
        """Get health insurance data using member_id."""
        return self.data.get(member_id, {})

class MockAPI1(MockAPI):
    """Mock health insurance API 1."""
    def __init__(self):
        super().__init__('data/data1.json')

class MockAPI2(MockAPI):
    """Mock health insurance API 2."""
    def __init__(self):
        super().__init__('data/data2.json')

class MockAPI3(MockAPI):
    """Mock health insurance API 3."""
    def __init__(self):
        super().__init__('data/data3.json')
