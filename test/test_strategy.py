#!/bin/python3

"""
Test suite for coalescing strategies.
"""

from coalesce.strategy import *
import unittest

class MinStrategyTestCase(unittest.TestCase):
    def setUp(self):
        self.strategy = MinStrategy

    def test_no_input(self):
        self.assertEqual(self.strategy.execute([]), {})

    def test_one_input(self):
        resp = [{'key1': 10, 'key2': 2, 'key3': 30}]
        self.assertEqual(self.strategy.execute(resp), resp[0])

    def test_empty_input(self):
        responses = [{'key1': 10, 'key2': 2, 'key3': 30}, {}]
        self.assertEqual(self.strategy.execute(responses), responses[0])

    def test_two_inputs(self):
        resp1 = {'key1': 10, 'key2': 2, 'key3': 30}
        resp2 = {'key1': 1, 'key2': 20, 'key3': 3}
        responses = [resp1, resp2]
        
        result = {'key1': 1, 'key2': 2, 'key3': 3}
        self.assertEqual(self.strategy.execute(responses), result)

class MaxStrategyTestCase(unittest.TestCase):
    def setUp(self):
        self.strategy = MaxStrategy

    def test_no_input(self):
        self.assertEqual(self.strategy.execute([]), {})

    def test_one_input(self):
        resp = [{'key1': 10, 'key2': 2, 'key3': 30}]
        self.assertEqual(self.strategy.execute(resp), resp[0])

    def test_empty_input(self):
        responses = [{'key1': 10, 'key2': 2, 'key3': 30}, {}]
        self.assertEqual(self.strategy.execute(responses), responses[0])

    def test_two_inputs(self):
        resp1 = {'key1': 10, 'key2': 2, 'key3': 30}
        resp2 = {'key1': 1, 'key2': 20, 'key3': 3}
        responses = [resp1, resp2]
        
        result = {'key1': 10, 'key2': 20, 'key3': 30}
        self.assertEqual(self.strategy.execute(responses), result)

class MeanStrategyTestCase(unittest.TestCase):
    def setUp(self):
        self.strategy = MeanStrategy

    def test_no_input(self):
        self.assertEqual(self.strategy.execute([]), {})

    def test_one_input(self):
        resp = [{'key1': 10, 'key2': 2, 'key3': 30}]
        self.assertEqual(self.strategy.execute(resp), resp[0])

    def test_empty_input(self):
        responses = [{'key1': 10, 'key2': 2, 'key3': 30}, {}]
        self.assertEqual(self.strategy.execute(responses), responses[0])

    def test_two_inputs(self):
        resp1 = {'key1': 10, 'key2': 2, 'key3': 30}
        resp2 = {'key1': 1, 'key2': 20, 'key3': 3}
        responses = [resp1, resp2]
        
        result = {'key1': 5, 'key2': 11, 'key3': 16}
        self.assertEqual(self.strategy.execute(responses), result)

class ModeStrategyTestCase(unittest.TestCase):
    def setUp(self):
        self.strategy = ModeStrategy

    def test_no_input(self):
        self.assertEqual(self.strategy.execute([]), {})

    def test_one_input(self):
        resp = [{'key1': 10, 'key2': 2, 'key3': 30}]
        self.assertEqual(self.strategy.execute(resp), resp[0])

    def test_empty_input(self):
        responses = [{'key1': 10, 'key2': 2, 'key3': 30}, {}]
        self.assertEqual(self.strategy.execute(responses), responses[0])

    def test_unique_inputs(self):
        resp1 = {'key1': 10, 'key2': 2, 'key3': 30}
        resp2 = {'key1': 1, 'key2': 20, 'key3': 3}
        responses = [resp1, resp2]
        
        self.assertEqual(self.strategy.execute(responses), responses[0])

    def test_not_unique_inputs(self):
        resp1 = {'key1': 10, 'key2': 2, 'key3': 30}
        resp2 = {'key1': 10, 'key2': 20, 'key3': 3}
        resp3 = {'key1': 1, 'key2': 2, 'key3': 3}
        responses = [resp1, resp2, resp3]
        
        result = {'key1': 10, 'key2': 2, 'key3': 3}
        self.assertEqual(self.strategy.execute(responses), result)

if __name__ == '__main__':
    unittest.main()
