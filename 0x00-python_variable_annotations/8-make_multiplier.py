#!/usr/bin/env python3
"""
  Complex types - function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
      make_multiplier - takes a float multiplier as argument,
      returns a function that multiplies a float by multiplier
    """

    def f(n: float) -> float:
        """ multiplies a float by multiplier """
        return float(n * multiplier)

    return f
