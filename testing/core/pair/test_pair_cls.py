"""Tests for joinplex.core.pair.Pair
"""
import pytest
from pandas import DataFrame
from pytest import param

from joinplex.core.pair import Pair


class SubTypeOfDF(DataFrame):  # pylint: disable=too-few-public-methods
    """A subclass of DataFrame for testing purposes."""


dfs_by_name = {
    "Empty DF": DataFrame(),
    "Non-empty DF": DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]}),
    "Subtype of DF": SubTypeOfDF(),
}
# Make copies so that they have same values but different object ids.
first_params = [param(df.copy(), id=name) for name, df in dfs_by_name.items()]
second_params = [param(df.copy(), id=name) for name, df in dfs_by_name.items()]


@pytest.fixture(scope="module", params=first_params)
def first_df(request):
    """A DataFrame to be used as the left df in a Pair."""
    return request.param


@pytest.fixture(scope="module", params=second_params)
def second_df(request):
    """A DataFrame to be used as the right df in a Pair."""
    return request.param


def test_pair_eq(first_df, second_df):
    """Test that two pairs are equal if they have the same left and right DataFrames."""
    left_df = first_df
    right_df = second_df
    pair1 = Pair(left_df, right_df)
    pair2 = Pair(left_df, right_df)
    assert pair1 == pair2


def test_pair_neq(first_df, second_df):
    """Test that two pairs are not equal if they have different left and right dfs."""
    pair1 = Pair(first_df, second_df)
    pair2 = Pair(second_df, first_df)
    assert pair1 != pair2


def test_non_df(first_df):
    """Test that a TypeError is raised if the left or right df is not a DataFrame."""
    non_df = "not a DataFrame"
    with pytest.raises(TypeError):
        Pair(first_df, non_df)
    with pytest.raises(TypeError):
        Pair(non_df, first_df)


def test_str_match_if_eq(first_df, second_df):
    """Test that the string representation of two equal pairs is the same."""
    pair1 = Pair(first_df, second_df)
    pair2 = Pair(first_df, second_df)
    assert pair1 == pair2
    assert str(pair1) == str(pair2)
