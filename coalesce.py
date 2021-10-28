#!/bin/python3

from mock import MockAPI1, MockAPI2, MockAPI3
from strategy import *

class CoalesceAPI:
    def __init__(self):
        self.apis = [MockAPI1(), MockAPI2(), MockAPI3()]
        self.strategy = AvgStrategy

    def set_strategy(strategy: Strategy) -> int:
        if strategy == Strategy.AVG:
            self.strategy = AvgStrategy
            return 0
        elif strategy == Strategy.MIN:
            self.strategy = MinStrategy
            return 0
        elif strategy == Strategy.MAX:
            self.strategy = MaxStrategy
            return 0
        else:
            return -1

    def get(self, member_id: str) -> dict:
        responses = []
        for api in self.apis:
            responses.append(api.get(member_id))

        return self.strategy.execute(responses)

if __name__ == '__main__':
    x = CoalesceAPI()
    print(x.get('1'))
