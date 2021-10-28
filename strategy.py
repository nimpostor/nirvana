#!/bin/python3

"""
Classes defining coalescing strategies for MockAPI responses.
"""

from enum import Enum
from collections import Counter, defaultdict

class Strategy(Enum):
    """Coalescing strategies currently supported."""
    MIN = 0
    MAX = 1
    MEAN = 2
    MODE = 3

class BaseStrategy:
    """Strategy template. Takes a list of API responses
    as argument, returns dict of coalesced data.
    """
    def execute(responses: list[dict]) -> dict:
        pass

class MinStrategy(BaseStrategy):
    """Uses minimum value of each response field."""
    def execute(responses):
        data = None
        for response in responses:
            if data is None:
                data = Counter(response)
            else:
                data &= Counter(response)
        return dict(data)

class MaxStrategy(BaseStrategy):
    """Uses maximum value of each response field."""
    def execute(responses):
        data = None
        for response in responses:
            if data is None:
                data = Counter(response)
            else:
                data |= Counter(response)
        return dict(data)

class MeanStrategy(BaseStrategy):
    """Uses average value of each response field."""
    def execute(responses):
        data = Counter()
        for response in responses:
            data += Counter(response)

        for k in data:
            data[k] //= len(responses)

        return dict(data)

class ModeStrategy(BaseStrategy):
    """Uses most common value of each response field."""
    def execute(responses):
        dd = defaultdict(list)
        for response in responses:
            for k, v in response.items():
                dd[k].append(v)
        
        data = { k : max(v, key=v.count) for (k, v) in dd.items() }
        return data
