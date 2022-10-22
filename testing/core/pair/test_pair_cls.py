"""Tests for joinplex.core.pair.Pair
"""
from pandas import DataFrame

from joinplex.core.pair import Pair


def test_pair_eq():
    """Test that two pairs are equal if they have the same left and right DataFrames."""
    left_df = DataFrame()
    right_df = DataFrame()
    pair1 = Pair(left_df, right_df)
    pair2 = Pair(left_df, right_df)
    assert pair1 == pair2


def test_pair_neq():
    """Test that two pairs are not equal if they have different left and right dfs."""
    first_df = DataFrame()
    second_df = DataFrame()
    pair1 = Pair(first_df, second_df)
    pair2 = Pair(second_df, first_df)
    assert pair1 != pair2
