"""Pairs of DataFrames to be joined.
"""
from dataclasses import dataclass

from pandas import DataFrame


@dataclass(frozen=True, eq=False, order=False, unsafe_hash=True)
class Pair:
    """A pair of DataFrames which are intended at some point to be joined together.

    Pairs are considered equal if they have identical left and right DataFrames: not
    in terms of values but in terms of object identity.

    Attributes:
        left_df: The left DataFrame.
        right_df: The right DataFrame.
    """

    left_df: DataFrame
    right_df: DataFrame

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, Pair):
            return False
        is_eq = (self.left_df is __o.left_df) and (self.right_df is __o.right_df)
        return is_eq
