#!/bin/python3

"""
API providing access to health insurance member data from mock APIs,
coalesced using a configurable strategy.
"""

from .mock import MockAPI1, MockAPI2, MockAPI3
from .strategy import *

class CoalesceAPI:
    """Class to coalesce and return data from mock APIs.
    Uses mean strategy as default.
    """

    def __init__(self):
        """Constructor."""
        self.apis = [MockAPI1(), MockAPI2(), MockAPI3()]
        self.strategy = MeanStrategy

    def set_strategy(self, strategy: Strategy) -> int:
        """Switch coalescing strategy during runtime.
        Returns 0 on success, -1 on failure.
        """

        # TODO: change to match statement
        if strategy == Strategy.MIN:
            self.strategy = MinStrategy
            return 0
        elif strategy == Strategy.MAX:
            self.strategy = MaxStrategy
            return 0
        elif strategy == Strategy.MEAN:
            self.strategy = MeanStrategy
            return 0
        elif strategy == Strategy.MODE:
            self.strategy = ModeStrategy
            return 0
        else:
            return -1

    def get(self, member_id: str) -> dict:
        """Get coalesced health insurance data using member_id."""
        responses = []
        for api in self.apis:
            responses.append(api.get(member_id))

        return self.strategy.execute(responses)
