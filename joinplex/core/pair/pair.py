"""Pairs of DataFrames to be joined.
"""
from dataclasses import dataclass

from pandas import DataFrame


@dataclass(frozen=True, eq=False, order=False, unsafe_hash=True, repr=False, init=True)
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

    def __post_init__(self) -> None:
        # Check that two paired objects are indeed both DataFrames.
        df_by_name = dict(left_df=self.left_df, right_df=self.right_df)
        for name, df in df_by_name.items():
            if not isinstance(df, DataFrame):
                raise TypeError(f"{name} must be a DataFrame, not a {type(df)}")

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, Pair):
            return False
        is_eq = (self.left_df is __o.left_df) and (self.right_df is __o.right_df)
        return is_eq

    def __str__(self) -> str:
        left_hexid = hex(id(self.left_df))
        right_hexid = hex(id(self.right_df))
        return f"Pair(df at {left_hexid}, df at {right_hexid})"

    def __repr__(self) -> str:
        return self.__str__()
