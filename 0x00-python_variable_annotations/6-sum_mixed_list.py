#!/usr/bin/env python3
from typing import Union, List
"""
  Complex types - mixed list
"""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sum a mixed list
    """

    return float(sum(mxd_lst))
