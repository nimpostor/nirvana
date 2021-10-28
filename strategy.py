#!/bin/python3

from enum import Enum
from collections import Counter

class Strategy(Enum):
    AVG = 0
    MIN = 1
    MAX = 2
    COUNT = 3

class BaseStrategy:
    def execute(responses: list[dict]) -> dict:
        pass

class AvgStrategy(BaseStrategy):
    def execute(responses):
        data = Counter()
        for response in responses:
            data += Counter(response)

        for k in data:
            data[k] //= len(responses)

        return dict(data)

class MinStrategy(BaseStrategy):
    def execute(responses):
        data = None
        for response in responses:
            if data is None:
                data = Counter(response)
            else:
                data &= Counter(response)
        return dict(data)

class MaxStrategy(BaseStrategy):
    def execute(responses):
        data = None
        for response in responses:
            if data is None:
                data = Counter(response)
            else:
                data |= Counter(response)
        return dict(data)
