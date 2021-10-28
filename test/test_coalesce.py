#!/bin/python3

"""
Test suite for CoalesceAPI.
"""

from coalesce.coalesce import CoalesceAPI
from coalesce.strategy import Strategy
import unittest

class CoalesceAPITestCase(unittest.TestCase):
    def setUp(self):
        self.api = CoalesceAPI()
        self.assertIsInstance(self.api, CoalesceAPI)

    def test_set_strategy(self):
        self.assertEqual(self.api.set_strategy(Strategy.MIN), 0)
        self.assertEqual(self.api.set_strategy(Strategy.MAX), 0)
        self.assertEqual(self.api.set_strategy(Strategy.MEAN), 0)
        self.assertEqual(self.api.set_strategy(Strategy.MODE), 0)
        self.assertEqual(self.api.set_strategy(-1), -1)

    def test_get_data_default(self):
        self.assertEqual(
            self.api.get('1'),
            {'deductible' : 1066, 'stop_loss' : 11000, 'oop_max' : 5666})

    def test_get_data_configured(self):
        self.api.set_strategy(Strategy.MAX)
        self.assertEqual(
            self.api.get('1'),
            {'deductible' : 1200, 'stop_loss' : 13000, 'oop_max' : 6000})

if __name__ == '__main__':
    unittest.main()
