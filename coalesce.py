#!/bin/python3

from mock import MockAPI1, MockAPI2, MockAPI3
from strategy import *

class CoalesceAPI:
    def __init__(self):
        self.apis = [MockAPI1(), MockAPI2(), MockAPI3()]

    def get(self, member_id, strategy=Strategy.AVG):
        responses = []
        for api in self.apis:
            responses.append(api.get(member_id))

        if strategy == Strategy.MIN:
            pass
            #return get_min(responses)
        elif strategy == Strategy.MAX:
            pass
            #return get_max(responses)
        elif strategy == Strategy.COUNT:
            pass
            #return get_max_count(responses)
        else:
            return AvgStrategy.execute(responses)

if __name__ == '__main__':
    x = CoalesceAPI()
    print(x.get('1'))
