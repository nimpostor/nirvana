#!/bin/python3

from mock import MockAPI1, MockAPI2, MockAPI3
from enum import Enum

class Strategy(Enum):
    AVG = 0
    MIN = 1
    MAX = 2
    COUNT = 3

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
            return self.get_avg(responses)

    def get_avg(self, responses):
        data = {}
        for response in responses:
            for k, v in response.items():
                if k not in data: data[k] = v
                else: data[k] += v
                
        for k, v in data.items():
            data[k] //= len(responses)
        return data

if __name__ == '__main__':
    x = CoalesceAPI()
    print(x.get('1'))
