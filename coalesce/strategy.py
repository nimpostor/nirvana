#!/bin/python3

"""
Classes defining coalescing strategies for MockAPI responses.

NOTE: All strategies support empty API responses (member_id not found),
but assume that when a response is received, all fields are present.
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
        data = {}
        for response in responses:
            if not response: continue

            if not data:
                data = Counter(response)
            else:
                data &= Counter(response)
        return dict(data)

class MaxStrategy(BaseStrategy):
    """Uses maximum value of each response field."""
    def execute(responses):
        data = {}
        for response in responses:
            if not response: continue

            if not data:
                data = Counter(response)
            else:
                data |= Counter(response)
        return dict(data)

class MeanStrategy(BaseStrategy):
    """Uses average value of each response field."""
    def execute(responses):
        data = {}
        numResponses = 0
        for response in responses:
            if not response: continue

            if not data:
                data = Counter(response)
            else:
                data += Counter(response)
            numResponses += 1

        if numResponses == 0:
            return data
        else:
            for k in data:
                data[k] //= numResponses
            return dict(data)

class ModeStrategy(BaseStrategy):
    """Uses most common value of each response field.
    If each value is unique, the first encountered value is used.
    """
    def execute(responses):
        dd = defaultdict(list)
        for response in responses:
            if not response: continue
            for k, v in response.items():
                dd[k].append(v)
        
        if not dd:
            return {}
        else:
            data = {k : max(v, key=v.count) for (k, v) in dd.items()}
            return data
